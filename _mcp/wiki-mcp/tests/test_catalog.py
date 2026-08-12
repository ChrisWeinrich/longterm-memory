from pathlib import Path

from wiki_mcp.catalog import by_state, documents, load_wiki_root, snippet_for


def write_page(root: Path, relative: str, *, state: str = "accepted", body: str = "Knowledge") -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"---\ntitle: {relative}\ntype: note\ntags: [mcp, wiki]\nstate: {state}\n---\n\n{body}\n",
        encoding="utf-8",
    )


def test_catalog_only_reads_valid_markdown_inside_allowed_directories(tmp_path: Path) -> None:
    write_page(tmp_path, "accepted.md")
    write_page(tmp_path, "draft.md", state="draft")
    write_page(tmp_path, "inbox/private.md")
    (tmp_path / "invalid.md").write_text("# no frontmatter", encoding="utf-8")

    items = documents(tmp_path)

    assert [item.relative_path for item in items] == ["accepted.md", "draft.md"]
    assert [item.relative_path for item in by_state(items)] == ["accepted.md"]
    assert [item.relative_path for item in by_state(items, include_drafts=True)] == ["accepted.md", "draft.md"]


def test_document_ids_are_deterministic_and_snippets_are_compact(tmp_path: Path) -> None:
    write_page(tmp_path, "sources/one.md", body="A long explanation about controlled MCP reading.")
    first = documents(tmp_path)[0]
    second = documents(tmp_path)[0]

    assert first.id == second.id
    assert first.id.startswith("wiki-")
    assert "controlled MCP" in snippet_for(first, "MCP")


def test_config_resolves_wiki_root_relative_to_config(tmp_path: Path) -> None:
    wiki = tmp_path / "wiki"
    wiki.mkdir()
    config = tmp_path / "_mcp" / "wiki-mcp.config.yaml"
    config.parent.mkdir()
    config.write_text("wiki_root: ../wiki\n", encoding="utf-8")

    assert load_wiki_root(config) == wiki.resolve()
