---
title: Map of Context
type: moc
tags: [context, navigation]
state: accepted
---

# Map of Context

## Purpose

This is the semantic orientation map for this repository. It complements the
filesystem, source code, and repository documentation; it does not replace
them.

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
`project-state` provides the descriptive inventory; `project-health` provides
the repository-wide, extensible validation and curation check.

<!-- moc:path=_mcp/wiki-mcp -->

Local stdio MCP for controlled access to accepted wiki knowledge and Raw
external-note handoff.

<!-- moc:path=wiki -->

Curated, durable project knowledge. Start at `wiki/index.md`; draft and
accepted and draft pages live in `wiki/pages/`.

<!-- moc:path=_raw -->

Immutable material awaiting curation, separated into `sources/`,
`conversations/`, `external/`, and `research/`. Read it, but never modify it.

<!-- moc:path=_research -->

Deep-research workspaces. Outline and query approval happen here; completed
reports are written to `_raw/research/` before later curation.

## Sources of truth

| Concern | Authoritative location |
| --- | --- |
| Repository rules | `AGENTS.md` |
| Project overview | `README.md` |
| Durable project knowledge | `wiki/` |
| Original source material | `_raw/` |
| Project skill definitions | `.agents/skills/` |
| Controlled wiki read interface | `_mcp/wiki-mcp/` |

## Relationships

- Raw material in `_raw/` is added to an existing curated page or forms a new
  draft in `wiki/`; curated `sources:` fields retain every used Raw path.
- Deep-research workspaces in `_research/` create completed reports in
  `_raw/research/`.
- `_templates/` provides the document shapes used by research and wiki
  workflows.

## Maintenance

Update this MOC when repository structure, major entry points, component
responsibilities, capabilities, sources of truth, workflows, or important
relationships change. Ordinary implementation changes inside an existing area
normally do not require an MOC update.
