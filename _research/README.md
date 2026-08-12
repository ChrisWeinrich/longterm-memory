---
title: Research workspace
type: instructions
tags: [research]
state: accepted
---

# Research workspace

Create one folder per deep-research topic: `_research/<topic-slug>/`.
Copy `research-outline.md` and `deep-research-query.md` from `_templates/` as
`outline.md` and `query.md`. Review and set both files to `state: accepted`
before starting research.

Fast shallow research runs directly and does not need a workspace. Completed
reports always go to `wiki/sources/` as `draft` pages. A reviewer must change
the state to `accepted` before a report appears in `wiki/index.md` or supports
an authoritative wiki answer.

## Required host capability

Before any research, verify that the host agent can run a web search and open a
result URL. This template deliberately does not embed provider credentials or a
browser integration: use the host agent's configured web/search tool. If the
check fails, configure that capability before continuing; do not conduct
research from unverified or inaccessible results.
