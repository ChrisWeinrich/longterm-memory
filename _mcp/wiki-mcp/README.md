---
title: Wiki MCP
type: documentation
tags: [mcp, wiki, agents]
state: accepted
---

# Kustos Wiki MCP

`wiki-mcp` is Kustos's local stdio MCP server for this project's map and curated
Markdown knowledge. Its dedicated orientation tool reads only the repository
`MOC.md`; its Wiki tools read only curated pages in `wiki/`. It never exposes
`_raw/`, `_research/`, local transcripts, configuration, or arbitrary paths.
Its single write tool can only create new external-note Raw material in
`_raw/external/` for later human curation.

Project-local artifact directories are also outside this interface. They can
remain Git-tracked and visible in Obsidian with a project-specific schema, but
they become MCP-readable only when reviewed knowledge is deliberately curated
into `wiki/`.

## Start

From the generated project root:

```sh
uv run --directory _mcp/wiki-mcp wiki-mcp
```

The server reads `_mcp/wiki-mcp.config.yaml`. It has no network listener or
secrets. Register this command with a local MCP client only after validating
the generated project; configure Codex, Claude, and Copilot together in their
shared configuration change.

## Copier customization

Copier asks for the MCP handshake text and the visible descriptions of every
tool and resource. These answers are rendered into `_mcp/wiki-mcp.texts.json`
and recorded in `.copier-answers.yml`; change them during creation or later
with `copier update`.

## Tools and resources

- `wiki_get_moc` returns the repository `MOC.md`. Start here when the task is
  unclear or you need to understand the project’s areas and sources of truth.
- `wiki_discover` shows the policy plus current document types and tags.
- `wiki_index` returns `wiki/index.md` and accepted page metadata.
- `wiki_search` searches accepted pages by default; `include_drafts: true`
  makes unreviewed drafts visible and labels them as such.
- `wiki_get` loads only a server-issued document ID, never a file path; a draft
  also requires explicit `include_drafts: true`.
- `wiki_submit_note` creates a new `type: external-note` Raw record in
  `_raw/external/` only. It cannot select a path, alter existing knowledge, or
  make content authoritative. The project-health check reports Raw entries
  that still need a curated `sources:` reference.
- `wiki://index`, `wiki://schema`, and `wiki://log` provide the active index,
  authority policy, and maintenance log.

Start with `wiki_get_moc` when you need project orientation, then use
`wiki_discover` or `wiki_index`, followed by `wiki_search` and `wiki_get`.
Use `wiki_submit_note` only to hand external context into the curation queue.
The MCP does not replace the `research`, `llm-wiki`, or `moc` skills.
