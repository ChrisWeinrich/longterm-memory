---
name: research
description: Plan accepted deep research or run a fast shallow search with verified web search and URL retrieval, then save the result as raw material for later wiki curation.
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
2. Copy `_templates/research-plan.md` to `outline.md` and
   `_templates/research-query.md` to `query.md`.
3. Fill both files. Do not start research unless both have `state: accepted`.
   If either is `draft`, stop and say which file needs review.
4. Research in this order: original or official sources and primary data;
   peer-reviewed research; reputable secondary analysis for context.
5. Copy `_templates/raw-research-report.md` to
   `_raw/research/<topic-slug>/report.md` and complete it. Keep it as raw
   material without `state`. Include source URLs, publication dates when
   available, uncertainty, and clearly label inference.

## Fast shallow research

Run it directly without an outline or query. Write the result to
`_raw/research/<topic-slug>--shallow/report.md` from
`_templates/raw-research-report.md`; use `type: raw-research-report` and no
`state`. Use the same source-quality rules and include a short sources section.

## Curate a report into the wiki

Every completed Raw research report is curated later, whether it is deep or
shallow research:

1. Check `wiki/index.md` and related `wiki/pages/` pages. Add the raw report
   path to an existing page's `sources:` list when it genuinely extends that
   knowledge; otherwise copy `_templates/wiki-research-report.md` to a new page in
   `wiki/pages/`, set `sources:` to the raw report path, and keep
   `state: draft`.
2. Add a page to `wiki/index.md` only after its state is `accepted`. Draft
   reports remain unindexed until review; archived reports are never indexed.
3. Append a concise dated entry to `wiki/log.md` when a curated draft is
   created or materially updated.
