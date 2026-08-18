---
title: "Kustos"
type: project
tags: [ai-assistant]
state: accepted
project_slug: "personal-long-term-memory"
---

# Kustos

A curated, local-first long-term memory for my assistants, research, decisions,
and durable personal knowledge. Kustos is the general knowledge keeper: the
shared, reviewed memory for information that may be useful across assistants.

## Start here

This vault is the durable, general memory layer for Christian's assistants. It
captures reviewed personal context, decisions, research, and working
conventions in plain Markdown, so the knowledge remains inspectable and useful
independent of any one assistant or tool. Specialized assistants may maintain
their own bounded knowledge spaces; only explicitly shared, reviewed knowledge
belongs in Kustos. Keep it deliberately small: add one clear capability at a
time, and keep each layer understandable before building the next.

## Obsidian

This project is an Obsidian vault with Templater configured to use
`_templates/`. Install and enable the community plugin **Templater** in
Obsidian once; its plugin code is intentionally not included in this
repository. Use `_templates/project-note.md` as the basis for general notes.

## LLM Wiki

The first LLM Wiki implementation is intentionally small. All uncurated input
starts in `_raw/`: `sources/`, `conversations/`, `external/`, or `research/`.
An agent later adds that input to an existing `wiki/pages/` page or creates a
new draft, maintains the active-page MOC in `wiki/index.md`, and records
curated changes in `wiki/log.md`. Only accepted pages appear in the active MOC
and support authoritative wiki answers; drafts remain available for review.
Raw input is immutable. See `.agents/skills/llm-wiki/SKILL.md` for curation.

Research reports and discussion summaries begin as Raw material. During
curation, related inputs may be combined in one Wiki draft through its
`sources:` list. Agents connect genuinely related pages with Obsidian
wikilinks; only a human review can make a page active, citable wiki knowledge.

## Wiki MCP

The generated project includes a local stdio MCP under `_mcp/wiki-mcp/`. Start
with its `wiki_discover`, `wiki_index`, or `wiki_search` tools when looking for
durable knowledge; it exposes accepted pages by default and labels explicit
draft results as unreviewed. Its only write tool queues external context in
`_raw/external/`. See `_mcp/wiki-mcp/README.md` for the start command and tool
overview. This MCP does not replace the `research` or `llm-wiki` skills.

## Agent skills

Codex discovers this project's skills directly in `.agents/skills/`.

Use `project-state` for a read-only inventory of accepted, draft, archived,
and other document counts. Use `project-health` for read-only validation of
required structure, frontmatter, wikilinks, the active wiki index, Raw-input
curation coverage, research readiness, and legacy inbox migration. Add small
scripts to the relevant skill rather than creating an ad-hoc manual checklist
when this project needs more metrics or invariants.

## Template updates

Commit `.copier-answers.yml`. It records this template and the selected answers
so the vault can receive future changes with `copier update`.

## Research prerequisite

Research requires an agent with enabled web search and URL retrieval. Before a
research run, verify both capabilities with a search and by opening one result;
if either is unavailable, configure the host agent's browser/search capability
or use an agent that provides it. See `_research/README.md` for details.

<!-- project-conventions:start -->

## Project conventions

- Christian owns review and acceptance of durable knowledge. Agents may create
  drafts, but must not promote them to `accepted` without explicit approval.
- `wiki/` is the source of truth for curated knowledge. Keep `wiki/index.md`
  limited to accepted pages; use `_raw/` for immutable source material and
  `_research/` for active research work.
- Use the local Wiki MCP for durable context before searching elsewhere. Use
  the repository skills to create notes, research, discussion summaries, and
  maintained wiki pages.
- Keep this vault portable and local-first: do not add hosted dependencies,
  automatic synchronisation, or secrets unless a concrete need is agreed and
  documented.

Keep this section below the marker so Copier's base documentation above can
update independently.

<!-- project-conventions:end -->
