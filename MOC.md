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
`project-state-health` provides the repository-wide, extensible state and
health report.

<!-- moc:path=_mcp/wiki-mcp -->

Local, read-only stdio MCP for controlled access to accepted wiki knowledge.

<!-- moc:path=wiki -->

Curated, durable project knowledge. Start at `wiki/index.md`; published
research reports, discussion summaries, and source pages live in
`wiki/sources/`.

<!-- moc:path=_raw -->

Immutable original material for wiki ingestion. Read it, but never modify it.

<!-- moc:path=_research -->

Deep-research workspaces. Accepted research is published to `wiki/sources/`.

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

- Original material in `_raw/` is ingested into curated pages in `wiki/`.
- Deep-research workspaces in `_research/` publish completed reports to
  `wiki/sources/`.
- `_templates/` provides the document shapes used by research and wiki
  workflows.

## Maintenance

Update this MOC when repository structure, major entry points, component
responsibilities, capabilities, sources of truth, workflows, or important
relationships change. Ordinary implementation changes inside an existing area
normally do not require an MOC update.
