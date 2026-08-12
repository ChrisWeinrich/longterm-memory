---
name: llm-wiki
description: Maintain a small, local Markdown wiki from immutable sources.
title: LLM Wiki
type: skill
tags: [wiki, research]
state: accepted
---

# LLM Wiki

This is a small, local-first wiki. It has three layers:

- `_raw/`: original material for first ingest. Read it, but never modify it.
- `wiki/`: agent-maintained Markdown pages. This is the working knowledge.
- `AGENTS.md`: the maintenance contract.

## Ingest a source

When asked to ingest a file from `_raw/`:

1. Read the source and check `wiki/index.md` for related pages.
2. Create or update one page in `wiki/sources/` from
   `_templates/wiki-source.md`. Use a stable, descriptive filename.
3. Keep the summary factual. Put interpretations, unanswered questions, and
   contradictions in the final section instead of presenting them as facts.
4. Add useful `[[wikilinks]]` to related wiki pages.
5. Update `wiki/index.md` with the page only when its state is `accepted`.
   Draft pages remain available for review but are not active wiki knowledge;
   archived pages are never indexed.
6. Append a concise dated entry to `wiki/log.md`.

## Answer a wiki question

1. Start with `wiki/index.md`, then read the relevant accepted wiki pages.
2. Answer from accepted pages and cite the supporting pages with
   `[[wikilinks]]`.
3. Do not use a draft as authoritative evidence. If a draft is useful context,
   label it explicitly as unreviewed and do not present its claims as durable
   wiki knowledge.
4. Read the original source only when the accepted wiki lacks the needed detail
   or the question calls for verification.
5. If the answer identifies a lasting contradiction or missing knowledge,
   update the relevant wiki page, index, and log.

## Boundaries

- Do not add a database, vector search, web server, automatic sync, or a typed
  knowledge graph to this first implementation.
- Keep one source page per source. Do not introduce topic or entity pages
  until source pages alone no longer make queries understandable.
- `state: archived` pages remain on disk but must not appear in the active
  index.
- `state: draft` pages remain on disk for review but must not appear in the
  active index or underpin an authoritative wiki answer.
