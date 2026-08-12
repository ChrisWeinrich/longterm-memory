from pathlib import Path

import asyncio
import json
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from wiki_mcp.server import DEFAULT_DISPLAY_TEXT, create_server


def test_server_exposes_read_only_wiki_capabilities(tmp_path: Path) -> None:
    wiki = tmp_path / "wiki"
    wiki.mkdir()
    (wiki / "index.md").write_text(
        "---\ntitle: Index\ntype: moc\ntags: [wiki]\nstate: accepted\n---\n\n# Index\n",
        encoding="utf-8",
    )
    (wiki / "log.md").write_text(
        "---\ntitle: Log\ntype: log\ntags: [wiki]\nstate: accepted\n---\n\n# Log\n",
        encoding="utf-8",
    )
    (wiki / "draft.md").write_text(
        "---\ntitle: Draft\ntype: note\ntags: [wiki]\nstate: draft\n---\n\n# Draft\n",
        encoding="utf-8",
    )
    config = tmp_path / "wiki-mcp.config.yaml"
    config.write_text("wiki_root: wiki\n", encoding="utf-8")
    text_config = {
        **DEFAULT_DISPLAY_TEXT,
        "handshake": "Use the configured project Wiki MCP first.",
        "wiki_search": "Search this configured knowledge base.",
    }
    (tmp_path / "wiki-mcp.texts.json").write_text(json.dumps(text_config), encoding="utf-8")

    server = create_server(config)

    assert server.name == "wiki_mcp"

    async def exercise() -> None:
        parameters = StdioServerParameters(
            command=sys.executable,
            args=["-m", "wiki_mcp.server", "--config", str(config)],
        )
        async with stdio_client(parameters) as (read_stream, write_stream):
            async with ClientSession(read_stream, write_stream) as client:
                initialized = await client.initialize()
                assert initialized.instructions is not None
                assert initialized.instructions == "Use the configured project Wiki MCP first."
                discovered = await client.call_tool("wiki_discover", {})
                assert discovered.structuredContent is not None
                assert discovered.structuredContent["root"] == "wiki/"

                tools = await client.list_tools()
                assert {tool.name: tool.description for tool in tools.tools} == {
                    "wiki_discover": text_config["wiki_discover"],
                    "wiki_index": text_config["wiki_index"],
                    "wiki_search": text_config["wiki_search"],
                    "wiki_get": text_config["wiki_get"],
                }

                search = await client.call_tool("wiki_search", {"query": "Index"})
                assert search.structuredContent is not None
                result = search.structuredContent["results"][0]
                assert result["state"] == "accepted"

                page = await client.call_tool("wiki_get", {"id": result["id"]})
                assert page.structuredContent is not None
                assert page.structuredContent["frontmatter"]["title"] == "Index"
                path_attempt = await client.call_tool("wiki_get", {"id": "../../etc/passwd"})
                assert path_attempt.isError

                drafts = await client.call_tool("wiki_search", {"query": "Draft", "include_drafts": True})
                assert drafts.structuredContent is not None
                draft_id = drafts.structuredContent["results"][0]["id"]
                blocked = await client.call_tool("wiki_get", {"id": draft_id})
                assert blocked.isError
                allowed = await client.call_tool("wiki_get", {"id": draft_id, "include_drafts": True})
                assert allowed.structuredContent is not None
                assert allowed.structuredContent["notice"] == "This draft is unreviewed and not authoritative."

                resources = await client.list_resources()
                assert {str(resource.uri): resource.description for resource in resources.resources} == {
                    "wiki://index": text_config["wiki_index_resource"],
                    "wiki://log": text_config["wiki_log_resource"],
                    "wiki://schema": text_config["wiki_schema_resource"],
                }
                schema = await client.read_resource("wiki://schema")
                assert "accepted" in schema.contents[0].text

    asyncio.run(exercise())
