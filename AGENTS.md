---
title: "Personal Long-Term Memory instructions"
type: instructions
tags: [ai-assistant]
state: accepted
project_slug: "personal-long-term-memory"
---

# Personal Long-Term Memory

This is a small, local-first foundation for coding agents. Keep it KISS: start
at the lowest useful level and add complexity only when a clear need demands
it.

## Copier base conventions

- Start with `MOC.md`, then the relevant area's `index.md`.
- Markdown documents use `title`, `type`, `tags`, and `state` frontmatter.
  Valid states are `draft`, `accepted`, and `archived`.
- Never commit secrets, local environment files, or generated caches.
- Keep `_raw/` immutable. Only accepted pages belong in `wiki/index.md`.
- Use the relevant skill for research, discussions, wiki maintenance, and note
  creation.
- For durable knowledge, first use the local Wiki MCP's `wiki_discover`,
  `wiki_index`, or `wiki_search` tools before broader filesystem search or web
  research. It exposes accepted wiki knowledge by default; drafts are
  unreviewed and require explicit opt-in.
- Connect genuinely related discussions, research reports, and wiki pages with
  `[[wikilinks]]`. Add links when creating or materially changing knowledge;
  consider reciprocal links only when they add context and are permitted by the
  page's review state.
- When a conversation yields durable context, confirmed decisions, a stable
  working approach, or important open questions, proactively create a
  reviewable discussion draft. If its relevance is unclear, propose the draft
  instead.

## Working in this repository

1. Orient before editing: read this file, `README.md`, and the relevant skill
   or template. Inspect the existing structure before adding a new one.
2. Preserve user work. Keep changes focused, avoid destructive commands, and
   never commit secrets, tokens, local environment files, or generated caches.
3. Prefer small, explicit implementations over frameworks or abstractions.
   Reuse the existing templates and skills before creating new conventions.
4. When adding a capability, update its documentation and agent instructions in
   the same change. Keep Markdown frontmatter valid and use `archived` rather
   than deleting knowledge that should remain available.
5. When changing code or configuration, run the smallest relevant validation.

<!-- project-conventions:start -->

## Project conventions

Add this project's agent-specific rules, workflows, integrations, and
operating constraints here. Keep this section below the marker so Copier base
conventions above can update independently.

<!-- project-conventions:end -->
