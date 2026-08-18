---
name: discussion
description: Capture relevant conversations as raw material for later wiki curation. Use when the user asks to discuss, capture an outcome, record a decision, or save a conversation summary; also use proactively when a conversation establishes durable context, confirmed decisions, stable working practices, or important open questions.
title: Discussion workflow
type: skill
tags: [discussion, wiki]
state: accepted
---

# Discussion workflow

Capture durable outcomes from a conversation without treating a transcript or
unreviewed interpretation as authoritative knowledge. The result starts as raw
material and is curated into a reviewable wiki draft only later.

## When to capture raw material

Use this workflow when the user asks to capture a discussion, decision, or
conversation summary. Also act proactively when the conversation has a clear
lasting value, such as confirmed consensus, an explicit decision, a stable
working approach, durable architecture or product context, or an important
open question.

When lasting value is clear, capture the raw summary. When relevance is uncertain,
briefly propose capturing one instead. Do not create a summary for transient
brainstorming, rejected alternatives, or routine status chatter.

## Create the summary

1. Read `wiki/index.md` and the relevant accepted pages in `wiki/pages/`.
   Identify related knowledge, duplicate coverage, and possible
   contradictions before writing.
2. Copy `_templates/raw-conversation.md` to
   `_raw/conversations/YYYY-MM-DD--<topic-slug>.md`. Keep `type:
   raw-conversation`, add a truthful `origin`, and use lowercase kebab-case
   tags that describe the content. Raw material has no `state`.
3. Record only the conversation's consensus, explicitly confirmed decisions,
   and clearly named open questions. Do not present reasoning trails, rejected
   alternatives, or uncertain claims as facts.
4. Include `## Entscheidungen` only if a decision was actually made or
   explicitly confirmed. Otherwise describe the current state and uncertainty
   under `## Konsens / aktueller Stand`.
5. Add useful Obsidian wikilinks to genuinely related accepted wiki pages when
   they add context. Do not modify an accepted page without the user's explicit
   approval.

## Conversation references

Store only the summary; never copy or version the full transcript. Add the
optional `conversation` frontmatter object only when every included value was
actually verified. It may contain `system`, `session_id`, `location`, and
`availability`. Do not invent a session ID, URL, local path, or `file://`
link. If no stable reference is available, omit `conversation`; if a known
reference is unavailable, set only truthful availability information.

The conversation reference supports traceability only. It is not an
authoritative source; after review, the accepted summary is authoritative.

## Curation boundary

Do not add raw conversation material to `wiki/index.md` or present it as wiki
knowledge. During later curation, first inspect existing `wiki/pages/`
pages: add the raw path to an existing page's `sources:` list when it genuinely
extends that page, or create a new `discussion` draft from
`_templates/wiki-discussion.md`. A human must review and accept any resulting wiki
page. One raw conversation may support more than one curated page.
