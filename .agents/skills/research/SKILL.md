---
name: research
description: Plan accepted deep research or run a fast shallow search with verified web search and URL retrieval, then publish a reviewable report into the wiki.
title: Research workflow
type: skill
tags: [research]
state: accepted
---

# Research workflow

Use this repository's research workflow. Keep research focused, cited, and
small enough to review.

## Required capability

Before gathering sources, verify that the current host agent can both search
the web and retrieve a result URL. Perform one focused search, then open one
result. If either capability is unavailable, stop before writing a report and
explain that the host needs a configured browser/search capability. Do not
invent sources or treat inaccessible search results as verified evidence.

## Deep research

1. Create `_research/<topic-slug>/`.
2. Copy `_templates/research-outline.md` to `outline.md` and
   `_templates/deep-research-query.md` to `query.md`.
3. Fill both files. Do not start research unless both have `state: accepted`.
   If either is `draft`, stop and say which file needs review.
4. Research in this order: original or official sources and primary data;
   peer-reviewed research; reputable secondary analysis for context.
5. Copy `_templates/research-report.md` to
   `wiki/sources/YYYY-MM-DD--<topic-slug>.md` and complete it. Keep its state
   as `draft` for review. Include source URLs, publication dates when
   available, uncertainty, and clearly label inference.
6. Log the draft as described below. It is not an active wiki page until a
   reviewer changes its state to `accepted`.

## Fast shallow research

Run it directly without an outline or query. Write the result to
`wiki/sources/YYYY-MM-DD--<topic-slug>--shallow.md` with `type:
shallow-research` and `state: draft`. Use the same source-quality rules and
include a short sources section. Log the draft as described below. It is not
an active wiki page until a reviewer changes its state to `accepted`.

## Publish a report into the wiki

Every completed research report in `wiki/sources/` is logged, whether it is
deep or shallow research:

1. Check `wiki/index.md` for related pages and add useful Obsidian wikilinks to
   the report.
2. Add the report to `wiki/index.md` only after its state is `accepted`.
   Draft reports remain unindexed until review; archived reports are never
   indexed.
3. Append a concise dated entry to `wiki/log.md`, identifying a draft as
   pending review.
