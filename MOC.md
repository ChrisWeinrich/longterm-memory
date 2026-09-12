---
title: Kustos Map of Context
type: moc
tags: [context, navigation]
state: accepted
---

# Kustos Map of Context

## Purpose

This is Kustos's semantic orientation map. It complements the filesystem,
source code, and repository documentation; it does not replace them. The
local Wiki MCP exposes it through `wiki_get_moc` for agent orientation.

## Start here

<!-- moc:path=AGENTS.md -->

Repository rules and the working contract for coding agents.

<!-- moc:path=README.md -->

Project purpose and the first human-facing orientation.

## Core areas

<!-- moc:path=_templates -->

Obsidian and research templates for consistent Markdown documents.

<!-- moc:path=.agents/skills -->

Project skills and their workflows, discovered directly by Codex.
`moc` curates this map; `project-state` provides the descriptive inventory;
`project-health` provides the repository-wide, extensible validation and
curation check.

<!-- moc:path=_context -->

Current, Git-tracked project context for operational facts such as people,
dates, preferences, and ongoing relationships. It is separate from Raw input
and curated Wiki knowledge; use the `context` skill to maintain it.

<!-- moc:path=_mcp/wiki-mcp -->

Kustos's local stdio MCP. `wiki_get_moc` returns this map for orientation;
the remaining tools provide controlled access to accepted Wiki knowledge and
Raw external-note handoff.

<!-- moc:path=wiki -->

Curated, durable project knowledge. Start at `wiki/index.md`; draft and
accepted and draft pages live in `wiki/pages/`.

<!-- moc:path=_raw -->

Immutable material awaiting curation, separated into `sources/`,
`conversations/`, `external/`, and `research/`. Read it, but never modify it.

<!-- moc:path=_research -->

Deep-research workspaces. Outline and query approval happen here; completed
reports are written to `_raw/research/` before later curation.

## Project-local domains

Projects may add top-level artifact directories for finished, canonical domain
documents with their own schemas. Record each directory here when it becomes a
source of truth: describe its owner, lifecycle, validation, and relationship
to Raw material and curated Wiki knowledge. Such directories remain visible in
Obsidian but are outside the Wiki MCP unless their content is deliberately
curated into `wiki/`.

## Sources of truth

| Concern | Authoritative location |
| --- | --- |
| Repository rules | `AGENTS.md` |
| Project overview | `README.md` |
| Current project-specific operational context | `_context/` |
| Durable project knowledge | `wiki/` |
| Original source material | `_raw/` |
| Project skill definitions | `.agents/skills/` |
| Kustos orientation and controlled Wiki interface | `_mcp/wiki-mcp/` |
| Project-local domain artifacts | Project-defined; document in this MOC |

## Relationships

- Raw material in `_raw/` is added to an existing curated page or forms a new
  draft in `wiki/`; curated `sources:` fields retain every used Raw path.
- Deep-research workspaces in `_research/` create completed reports in
  `_raw/research/`.
- `_templates/` provides the document shapes used by research and wiki
  workflows.
- Agents use `wiki_get_moc` for Kustos orientation, then use
  `wiki_discover`/`wiki_index`, `wiki_search`, and `wiki_get` only as needed.
- `_context/` provides current operational context but is neither Raw input nor
  curated Wiki knowledge; reusable reference knowledge is curated into `wiki/`
  deliberately.
- Project-local domain artifacts may be derived from Raw material or produce
  knowledge worth curating into `wiki/`, but neither direction is automatic.

## Maintenance

Update this MOC when repository structure, major entry points, component
responsibilities, capabilities, sources of truth, workflows, or important
relationships change. Ordinary implementation changes inside an existing area
normally do not require an MOC update.
