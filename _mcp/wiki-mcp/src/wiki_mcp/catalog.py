"""Safe, small Markdown catalog used by the wiki MCP transport."""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
import re
from typing import Any, Iterable

import yaml


VALID_STATES = ("draft", "accepted", "archived")
REQUIRED_FRONTMATTER = ("title", "type", "tags", "state")
EXCLUDED_DIRECTORY_NAMES = {".git", "_raw", "raw", "inbox", "_research"}


class WikiError(ValueError):
    """A configuration or client-safe wiki error."""


@dataclass(frozen=True)
class Document:
    """A valid Markdown wiki page, indexed only by an opaque ID."""

    id: str
    relative_path: str
    frontmatter: dict[str, Any]
    body: str

    @property
    def title(self) -> str:
        return self.frontmatter["title"]

    @property
    def type(self) -> str:
        return self.frontmatter["type"]

    @property
    def tags(self) -> list[str]:
        return self.frontmatter["tags"]

    @property
    def state(self) -> str:
        return self.frontmatter["state"]

    @property
    def authority(self) -> str:
        return "authoritative" if self.state == "accepted" else "unreviewed"


def load_wiki_root(config_path: Path) -> Path:
    """Load a relative wiki root from a small, explicit YAML configuration."""
    try:
        config = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    except OSError as error:
        raise WikiError("Wiki configuration is unavailable. Check the --config path.") from error
    except yaml.YAMLError as error:
        raise WikiError("Wiki configuration is invalid YAML. Set wiki_root to a directory.") from error

    if not isinstance(config, dict) or not isinstance(config.get("wiki_root"), str):
        raise WikiError("Wiki configuration must contain a string wiki_root.")

    root = (config_path.parent / config["wiki_root"]).resolve()
    if not root.is_dir():
        raise WikiError("Configured wiki_root does not exist or is not a directory.")
    return root


def _parse_markdown(path: Path, root: Path) -> Document | None:
    try:
        resolved = path.resolve(strict=True)
        resolved.relative_to(root)
        text = resolved.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError, ValueError):
        return None

    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n?(.*)\Z", text, flags=re.DOTALL)
    if not match:
        return None
    try:
        frontmatter = yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None
    if not _valid_frontmatter(frontmatter):
        return None

    relative_path = resolved.relative_to(root).as_posix()
    document_id = "wiki-" + sha256(relative_path.encode("utf-8")).hexdigest()[:16]
    return Document(document_id, relative_path, frontmatter, match.group(2))


def _valid_frontmatter(frontmatter: object) -> bool:
    if not isinstance(frontmatter, dict) or any(key not in frontmatter for key in REQUIRED_FRONTMATTER):
        return False
    if not all(isinstance(frontmatter[key], str) and frontmatter[key].strip() for key in ("title", "type")):
        return False
    if frontmatter["state"] not in VALID_STATES:
        return False
    return isinstance(frontmatter["tags"], list) and all(
        isinstance(tag, str) and tag.strip() for tag in frontmatter["tags"]
    )


def documents(root: Path) -> list[Document]:
    """Return all valid, allowed wiki pages without following outside symlinks."""
    result: list[Document] = []
    for path in root.rglob("*.md"):
        relative_parts = path.relative_to(root).parts
        if any(part in EXCLUDED_DIRECTORY_NAMES or part.startswith(".") for part in relative_parts):
            continue
        document = _parse_markdown(path, root)
        if document is not None:
            result.append(document)
    return sorted(result, key=lambda document: document.relative_path)


def by_state(items: Iterable[Document], *, include_drafts: bool = False, all_states: bool = False) -> list[Document]:
    """Apply the authority policy shared by every tool."""
    if all_states:
        return list(items)
    allowed_states = {"accepted", "draft"} if include_drafts else {"accepted"}
    return [item for item in items if item.state in allowed_states]


def document_summary(document: Document, *, snippet: str | None = None) -> dict[str, Any]:
    """Return intentionally compact metadata suitable for tool results."""
    result: dict[str, Any] = {
        "id": document.id,
        "title": document.title,
        "type": document.type,
        "tags": document.tags,
        "state": document.state,
        "authority": document.authority,
    }
    if snippet is not None:
        result["snippet"] = snippet
    return result


def snippet_for(document: Document, query: str) -> str:
    """Build a short, whitespace-normalized excerpt around a query match."""
    text = re.sub(r"\\s+", " ", document.body).strip()
    position = text.casefold().find(query.casefold())
    if position < 0:
        return text[:240] + ("…" if len(text) > 240 else "")
    start = max(0, position - 90)
    end = min(len(text), position + len(query) + 150)
    return ("…" if start else "") + text[start:end] + ("…" if end < len(text) else "")
