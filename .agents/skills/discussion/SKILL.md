---
name: discussion
description: Turn relevant conversations into short, reviewable wiki drafts. Use when the user asks to discuss, capture an outcome, record a decision, or save a conversation summary; also use proactively when a conversation establishes durable context, confirmed decisions, stable working practices, or important open questions.
title: Discussion workflow
type: skill
tags: [discussion, wiki]
state: accepted
---

# Discussion workflow

Capture durable outcomes from a conversation without treating a transcript or
unreviewed interpretation as authoritative knowledge. The result is always a
human-reviewable draft.

## When to create a draft

Use this workflow when the user asks to capture a discussion, decision, or
conversation summary. Also act proactively when the conversation has a clear
lasting value, such as confirmed consensus, an explicit decision, a stable
working approach, durable architecture or product context, or an important
open question.

When lasting value is clear, create the draft. When relevance is uncertain,
briefly propose creating one instead. Do not create a draft for transient
brainstorming, rejected alternatives, or routine status chatter.

## Create the summary

1. Read `wiki/index.md` and the relevant accepted pages in `wiki/sources/`.
   Identify related knowledge, duplicate coverage, and possible
   contradictions before writing.
2. Copy `_templates/discussion.md` to
   `wiki/sources/YYYY-MM-DD--<topic-slug>.md`. Keep `type: discussion` and
   `state: draft`; use lowercase kebab-case tags that describe the content.
   Keep `wiki/sources/` flat.
3. Record only the conversation's consensus, explicitly confirmed decisions,
   and clearly named open questions. Do not present reasoning trails, rejected
   alternatives, or uncertain claims as facts.
4. Include `## Entscheidungen` only if a decision was actually made or
   explicitly confirmed. Otherwise describe the current state and uncertainty
   under `## Konsens / aktueller Stand`.
5. Add useful Obsidian wikilinks to genuinely related research reports,
   discussions, and accepted wiki pages. Consider a reciprocal link when it
   adds meaningful context, but do not modify an accepted page without the
   user's explicit approval.
6. Add a concise dated entry to `wiki/log.md` that identifies the discussion
   as a draft pending human review.

## Conversation references

Store only the summary; never copy or version the full transcript. Add the
optional `conversation` frontmatter object only when every included value was
actually verified. It may contain `system`, `session_id`, `location`, and
`availability`. Do not invent a session ID, URL, local path, or `file://`
link. If no stable reference is available, omit `conversation`; if a known
reference is unavailable, set only truthful availability information.

The conversation reference supports traceability only. It is not an
authoritative source; after review, the accepted summary is authoritative.

## Review boundary

Do not add this draft to `wiki/index.md`, change it to `accepted`, or present
it as authoritative wiki knowledge. A human must review and accept it first.
Do not change existing accepted knowledge pages as part of this workflow
without explicit user approval.
