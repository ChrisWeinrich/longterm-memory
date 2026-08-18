---
title: Research workspace
type: instructions
tags: [research]
state: accepted
---

# Research workspace

Create one folder per deep-research topic: `_research/<topic-slug>/`.
Copy `research-plan.md` and `research-query.md` from `_templates/` as
`outline.md` and `query.md`. Review and set both files to `state: accepted`
before starting research.

Fast shallow research runs directly and does not need an outline or query.
Completed deep and shallow reports go to `_raw/research/` without a state.
During later curation, a report may extend an existing `wiki/pages/` page or
support a new draft. A reviewer must accept a curated page before it appears in
`wiki/index.md` or supports an authoritative wiki answer.

## Required host capability

Before any research, verify that the host agent can run a web search and open a
result URL. This template deliberately does not embed provider credentials or a
browser integration: use the host agent's configured web/search tool. If the
check fails, configure that capability before continuing; do not conduct
research from unverified or inaccessible results.
