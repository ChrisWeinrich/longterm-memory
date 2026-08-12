"""stdio MCP transport for controlled access to a local curated wiki."""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path
import re
from typing import Any, Literal

from mcp.server.fastmcp import FastMCP
from pydantic import Field
import yaml

from .catalog import VALID_STATES, WikiError, by_state, document_summary, documents, load_wiki_root, snippet_for


DEFAULT_DISPLAY_TEXT = {
    "handshake": (
        "Use this read-only MCP to find curated project knowledge. Start with wiki_discover or wiki_index, "
        "then search and retrieve only the context you need. Accepted pages are authoritative; drafts require "
        "explicit opt-in and are always unreviewed."
    ),
    "wiki_discover": "Describe the current wiki policy, document types, tags, and collections.",
    "wiki_index": "Return the active wiki index and compact metadata for accepted pages.",
    "wiki_search": "Search allowed wiki content with simple, explainable case-insensitive text matching.",
    "wiki_get": "Get one wiki page by server-issued ID; file paths are never accepted.",
    "wiki_submit_note": "Save externally supplied context as an unreviewed draft in the wiki inbox for human curation.",
    "wiki_index_resource": "The accepted wiki navigation page.",
    "wiki_schema_resource": "The wiki frontmatter and authority policy.",
    "wiki_log_resource": "The accepted wiki maintenance log.",
}


def load_display_text(config_path: Path) -> dict[str, str]:
    """Load Copier-rendered MCP text, with safe defaults for programmatic use."""
    text_path = config_path.parent / "wiki-mcp.texts.json"
    if not text_path.is_file():
        return DEFAULT_DISPLAY_TEXT
    try:
        configured = json.loads(text_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise WikiError("MCP text configuration is invalid. Regenerate wiki-mcp.texts.json with Copier.") from error
    if not isinstance(configured, dict) or set(configured) != set(DEFAULT_DISPLAY_TEXT):
        raise WikiError("MCP text configuration must define every handshake, tool, and resource description.")
    if not all(isinstance(value, str) and value.strip() for value in configured.values()):
        raise WikiError("MCP handshake and descriptions must be non-empty text.")
    return configured


def _slug(value: str) -> str:
    """Make a short filesystem-safe name without accepting a client path."""
    slug = re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")
    return slug[:80] or "external-note"


def _write_inbox_note(wiki_root: Path, *, title: str, content: str, tags: list[str]) -> Path:
    """Write one externally supplied draft under the fixed inbox directory only."""
    inbox = (wiki_root / "inbox").resolve()
    try:
        inbox.relative_to(wiki_root)
    except ValueError as error:  # Defensive guard for unusual symlinked vaults.
        raise WikiError("The wiki inbox must resolve inside the configured wiki root.") from error
    inbox.mkdir(parents=True, exist_ok=True)

    received_at = datetime.now(timezone.utc).replace(microsecond=0)
    frontmatter = {
        "title": title.strip(),
        "type": "external-note",
        "tags": ["external", "inbox", *tags],
        "state": "draft",
        "origin": "wiki-mcp",
        "received_at": received_at.isoformat().replace("+00:00", "Z"),
    }
    document = f"---\n{yaml.safe_dump(frontmatter, allow_unicode=True, sort_keys=False)}---\n\n# {title.strip()}\n\n{content.strip()}\n"
    prefix = f"{received_at.strftime('%Y-%m-%d--%H%M%S')}--{_slug(title)}"
    for suffix in range(1, 1_000):
        candidate = inbox / f"{prefix}{'' if suffix == 1 else f'--{suffix}'}.md"
        try:
            with candidate.open("x", encoding="utf-8") as file:
                file.write(document)
            return candidate
        except FileExistsError:
            continue
    raise WikiError("Could not allocate an inbox note filename. Resolve existing inbox filename collisions.")


def create_server(config_path: Path) -> FastMCP:
    """Create the server; catalog reads are intentionally fresh for each request."""
    wiki_root = load_wiki_root(config_path)
    text = load_display_text(config_path)
    mcp = FastMCP(
        "wiki_mcp",
        instructions=text["handshake"],
    )
    annotations = {
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": False,
    }
    write_annotations = {
        "readOnlyHint": False,
        "destructiveHint": False,
        "idempotentHint": False,
        "openWorldHint": False,
    }

    def catalog() -> list:
        return documents(wiki_root)

    @mcp.tool(
        name="wiki_discover",
        description=text["wiki_discover"],
        annotations=annotations,
    )
    def wiki_discover(
        scope: Literal["accepted", "all"] = "accepted",
    ) -> dict[str, Any]:
        """Return the current wiki policy, document types, tags, and collections."""
        items = by_state(catalog(), all_states=scope == "all")
        type_counts = Counter(item.type for item in items)
        tag_counts = Counter(tag for item in items for tag in item.tags)
        return {
            "root": "wiki/",
            "scope": scope,
            "frontmatter_schema": {
                "required": ["title", "type", "tags", "state"],
                "state_values": list(VALID_STATES),
            },
            "types": [{"value": value, "count": count} for value, count in sorted(type_counts.items())],
            "tags": [{"value": value, "count": count} for value, count in sorted(tag_counts.items())],
            "search_defaults": {"states": ["accepted"], "drafts_authoritative": False},
            "collections": [{"id": "durable-knowledge", "roots": ["wiki/"], "states": ["accepted"]}],
        }

    @mcp.tool(
        name="wiki_index",
        description=text["wiki_index"],
        annotations=annotations,
    )
    def wiki_index() -> dict[str, Any]:
        """Return the active wiki index and compact metadata for accepted pages."""
        items = by_state(catalog())
        index = next((item for item in items if item.relative_path == "index.md"), None)
        if index is None:
            raise WikiError("wiki/index.md must be a valid accepted Markdown page.")
        return {
            "index": {"frontmatter": index.frontmatter, "content": index.body},
            "pages": [document_summary(item) for item in items],
        }

    @mcp.tool(
        name="wiki_search",
        description=text["wiki_search"],
        annotations=annotations,
    )
    def wiki_search(
        query: str = Field(min_length=1, max_length=500, description="Text to find in titles, tags, or Markdown content."),
        tags: list[str] | None = Field(default=None, max_length=20, description="Optional tags; every supplied tag must match."),
        type: str | None = Field(default=None, max_length=100, description="Optional exact document type."),
        include_drafts: bool = Field(default=False, description="Include drafts as explicitly unreviewed evidence."),
        limit: int = Field(default=10, ge=1, le=50, description="Maximum number of results."),
    ) -> dict[str, Any]:
        """Search allowed wiki content with case-insensitive text matching."""
        normalized_query = query.strip()
        if not normalized_query:
            raise WikiError("query must contain visible text.")
        requested_tags = {tag.strip().casefold() for tag in tags or [] if tag.strip()}
        matches = []
        for item in by_state(catalog(), include_drafts=include_drafts):
            item_tags = {tag.casefold() for tag in item.tags}
            searchable = "\n".join([item.title, " ".join(item.tags), item.body]).casefold()
            if normalized_query.casefold() not in searchable:
                continue
            if requested_tags and not requested_tags.issubset(item_tags):
                continue
            if type is not None and item.type != type.strip():
                continue
            matches.append(document_summary(item, snippet=snippet_for(item, normalized_query)))
        return {
            "query": normalized_query,
            "include_drafts": include_drafts,
            "total_count": len(matches),
            "count": min(len(matches), limit),
            "results": matches[:limit],
        }

    @mcp.tool(
        name="wiki_get",
        description=text["wiki_get"],
        annotations=annotations,
    )
    def wiki_get(
        id: str = Field(min_length=5, max_length=100, description="A document ID returned by a wiki MCP tool."),
        include_drafts: bool = Field(default=False, description="Allow a draft returned by an explicit draft-aware search."),
    ) -> dict[str, Any]:
        """Get one wiki page by server-issued ID; file paths are never accepted.

        Accepted pages are authoritative. A draft ID requires ``include_drafts`` to
        be explicitly true and remains clearly marked as unreviewed.
        """
        item = next((document for document in catalog() if document.id == id), None)
        if item is None:
            raise WikiError("Unknown wiki document ID. Use wiki_search or wiki_index to obtain an ID.")
        if item.state == "draft" and not include_drafts:
            raise WikiError("This document is a draft. Repeat with include_drafts=true to read unreviewed content.")
        return {
            "document": document_summary(item),
            "frontmatter": item.frontmatter,
            "content": item.body,
            "notice": "This draft is unreviewed and not authoritative." if item.state == "draft" else None,
        }

    @mcp.tool(
        name="wiki_submit_note",
        description=text["wiki_submit_note"],
        annotations=write_annotations,
    )
    def wiki_submit_note(
        title: str = Field(min_length=1, max_length=200, description="Short title for the externally supplied note."),
        content: str = Field(min_length=1, max_length=20_000, description="Markdown content to queue for human curation."),
        tags: list[str] | None = Field(default=None, max_length=20, description="Optional lowercase tags describing the note."),
    ) -> dict[str, Any]:
        """Queue external context in wiki/inbox only; it is never curated or authoritative."""
        normalized_title = title.strip()
        normalized_content = content.strip()
        if not normalized_title or not normalized_content:
            raise WikiError("title and content must contain visible text.")
        requested_tags = [tag.strip().casefold() for tag in tags or [] if tag.strip()]
        if any(not re.fullmatch(r"[a-z0-9][a-z0-9-]*", tag) for tag in requested_tags):
            raise WikiError("tags must use lowercase letters, digits, and dashes.")
        path = _write_inbox_note(
            wiki_root,
            title=normalized_title,
            content=normalized_content,
            tags=list(dict.fromkeys(requested_tags)),
        )
        return {
            "status": "queued_for_curation",
            "type": "external-note",
            "state": "draft",
            "origin": "wiki-mcp",
            "path": path.relative_to(wiki_root).as_posix(),
            "notice": "This external note is unreviewed and is not authoritative wiki knowledge.",
        }

    @mcp.resource(
        "wiki://index",
        description=text["wiki_index_resource"],
    )
    def wiki_index_resource() -> str:
        """The accepted wiki navigation page."""
        index = next((item for item in by_state(catalog()) if item.relative_path == "index.md"), None)
        if index is None:
            raise WikiError("wiki/index.md must be a valid accepted Markdown page.")
        return index.body

    @mcp.resource(
        "wiki://schema",
        description=text["wiki_schema_resource"],
    )
    def wiki_schema_resource() -> str:
        """The wiki frontmatter and authority policy."""
        return json.dumps(
            {
                "required_frontmatter": ["title", "type", "tags", "state"],
                "state_values": list(VALID_STATES),
                "authority_rule": "Only state: accepted is authoritative. Drafts require explicit opt-in and are unreviewed.",
            },
            indent=2,
        )

    @mcp.resource(
        "wiki://log",
        description=text["wiki_log_resource"],
    )
    def wiki_log_resource() -> str:
        """The accepted wiki maintenance log."""
        log = next((item for item in by_state(catalog()) if item.relative_path == "log.md"), None)
        if log is None:
            raise WikiError("wiki/log.md must be a valid accepted Markdown page.")
        return log.body

    return mcp


def main() -> None:
    """Run the local server over stdio without writing to stdout."""
    default_config = Path(__file__).resolve().parents[2] / "wiki-mcp.config.yaml"
    parser = argparse.ArgumentParser(description="Local MCP server for curated wiki reads and inbox-only external notes.")
    parser.add_argument("--config", type=Path, default=default_config, help="Path to wiki-mcp.config.yaml")
    args = parser.parse_args()
    create_server(args.config.resolve()).run()


if __name__ == "__main__":
    main()
