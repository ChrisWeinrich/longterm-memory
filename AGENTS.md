---
title: "Kustos instructions"
type: instructions
tags: [ai-assistant]
state: accepted
project_slug: "kustos"
---

# Kustos

Kustos is a small, local-first knowledge keeper for coding agents. Keep it
KISS: start at the lowest useful level and add complexity only when a clear
need demands it.

## Copier base conventions

- Start with `MOC.md`, then the relevant area's `index.md`. When using the
  local Wiki MCP for orientation, call `wiki_get_moc` first.
- Curated Markdown documents use `title`, `type`, `tags`, and `state`
  frontmatter. Valid states are `draft`, `accepted`, and `archived`.
- Managed Raw Markdown under `_raw/` uses `title`, `type`, `tags`, `origin`,
  and `created` or `received_at`; Raw material has no `state`.
- Keep unmodified sources, conversation captures, and research results in
  `_raw/`; they are not authoritative knowledge. Keep reviewed, general
  reference knowledge in `wiki/`. A project may also define its own
  Git-tracked artifact directories for finished, canonical domain documents.
  Document each such directory's schema, owner, lifecycle, and source of
  truth in the project's README and MOC. They are not Wiki MCP content unless
  the project explicitly curates knowledge into `wiki/`.
- Keep current project-specific operational facts in `_context/` when they
  help agents work effectively. It is Git-tracked but never a place for
  secrets, Raw source material, or authoritative Wiki knowledge. Use the
  `context` skill to read it when relevant; create or update facts only at the
  user's explicit request or confirmation.
- Never commit secrets, local environment files, or generated caches.
- Keep `_raw/` immutable. Only accepted pages belong in `wiki/index.md`.
- Use the relevant skill for research, discussions, wiki maintenance, and note
  creation. Use the `moc` skill when a material repository-structure,
  capability, responsibility, or source-of-truth change requires MOC curation.
- Use `project-state` for a descriptive repository inventory. Use
  `project-health` to validate repository-wide conventions and curation
  completeness; run every script in its `scripts/` directory. Add a small,
  deterministic health check there as this project gains new invariants.
- For durable knowledge, first use the local Wiki MCP. Call `wiki_get_moc`
  when project orientation is needed, then use `wiki_discover`, `wiki_index`,
  or `wiki_search` before broader filesystem search or web research. It
  exposes accepted wiki knowledge by default; drafts are unreviewed and require
  explicit opt-in.
- The Wiki MCP may queue externally supplied context only in `_raw/external/`
  as an `external-note` without a state. Do not treat Raw input as knowledge;
  a human must curate it into `wiki/pages/` before it can become accepted.
- Connect genuinely related discussions, research reports, and wiki pages with
  Obsidian wikilinks. Add links when creating or materially changing knowledge;
  consider reciprocal links only when they add context and are permitted by the
  page's review state.
- When a conversation yields durable context, confirmed decisions, a stable
  working approach, or important open questions, proactively capture a Raw
  conversation summary. If its relevance is unclear, propose the capture
  instead.

## Working in this repository

1. Orient before editing: read this file, `README.md`, and the relevant skill
   or template. Inspect the existing structure before adding a new one.
2. Preserve user work. Keep changes focused, avoid destructive commands, and
   never commit secrets, tokens, local environment files, or generated caches.
3. Prefer small, explicit implementations over frameworks or abstractions.
   Reuse the existing templates and skills before creating new conventions.
4. When adding a capability or domain artifact directory, update its
   documentation and agent instructions in the same change. Keep Wiki
   frontmatter valid and use `archived` rather than deleting knowledge that
   should remain available.
5. When changing code or configuration, run the smallest relevant validation.

<!-- project-conventions:start -->

## Project conventions

- Christian is the human reviewer for durable Kustos knowledge. Create new knowledge
  as a `draft` and never change it to `accepted` without explicit approval.
- Treat `wiki/` as the curated source of truth, `_raw/` as immutable input,
  and `_research/` as a workspace. Keep `wiki/index.md` restricted to accepted
  pages.
- Query the local Wiki MCP before broader search when durable context may
  exist. Follow the repository skills for notes, research, discussions, and
  wiki maintenance.
- Preserve the vault's local-first, portable design. Do not add hosted
  services, automatic synchronisation, secrets, or unnecessary infrastructure
  without explicit approval and matching documentation.

Keep this section below the marker so Copier base conventions above can update
independently.

<!-- project-conventions:end -->
