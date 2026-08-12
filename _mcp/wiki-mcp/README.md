---
title: Wiki MCP
type: documentation
tags: [mcp, wiki, agents]
state: accepted
---

# Wiki MCP

`wiki-mcp` is a local, read-only stdio MCP server for this project's curated
Markdown knowledge. It reads only `wiki/`; it never exposes `_raw/`, `raw/`,
`inbox/`, `_research/`, local transcripts, configuration, or arbitrary paths.

## Start

From the generated project root:

```sh
uv run --directory _mcp/wiki-mcp wiki-mcp
```

The server reads `_mcp/wiki-mcp.config.yaml`. It has no network listener,
secrets, or write tools. Register this command with a local MCP client only
after validating the generated project; configure Codex, Claude, and Copilot
together in their shared configuration change.

## Copier customization

Copier asks for the MCP handshake text and the visible descriptions of every
tool and resource. These answers are rendered into `_mcp/wiki-mcp.texts.json`
and recorded in `.copier-answers.yml`; change them during creation or later
with `copier update`.

## Tools and resources

- `wiki_discover` shows the policy plus current document types and tags.
- `wiki_index` returns `wiki/index.md` and accepted page metadata.
- `wiki_search` searches accepted pages by default; `include_drafts: true`
  makes unreviewed drafts visible and labels them as such.
- `wiki_get` loads only a server-issued document ID, never a file path; a draft
  also requires explicit `include_drafts: true`.
- `wiki://index`, `wiki://schema`, and `wiki://log` provide the active index,
  authority policy, and maintenance log.

Start with `wiki_discover` or `wiki_index`, then use `wiki_search` and
`wiki_get`. The MCP is a controlled reading interface; it does not replace the
`research` or `llm-wiki` skills.
