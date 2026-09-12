---
name: context
description: Read and maintain the rendered project's `_context/` notes when a request depends on current project-specific facts such as people, dates, preferences, ongoing relationships, or operational details. Use this skill whenever the user asks about or asks to record such context, even if they do not name `_context/`.
title: Kustos context
type: skill
tags: [context, project]
state: accepted
---

# Kustos context

`_context/` holds current Kustos-specific operational facts that help with
day-to-day work. It is deliberately lightweight: notes may use the structure
that best fits their purpose.

## Read context

When a request could depend on people, dates, preferences, recurring details,
or external relationships, inspect the relevant `_context/` notes before
answering or acting. Read only the context needed for the request and describe
uncertainty when a note is missing, stale, or conflicting.

## Maintain context

Create or update a context note only when the user explicitly asks or confirms
the factual content. Preserve existing facts, record dates or status when they
are known, and do not infer or invent personal details. Ask for clarification
when a proposed change would overwrite, contradict, or ambiguously replace an
existing fact.

## Boundaries

Keep credentials, tokens, and other secrets out of `_context/`. Do not place
raw source material here, do not add its notes to `wiki/index.md`, and do not
present them as curated Wiki knowledge. Deliberately curate reusable reference
knowledge into `wiki/` through the existing Wiki workflow when that is needed.
