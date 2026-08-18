---
name: create-note
description: Create a new Markdown note from the vault's standard Obsidian frontmatter template.
title: Create note
type: skill
tags: [obsidian, notes]
state: accepted
---

# Create note

Use `_templates/project-note.md` as the basis for every new general note.

When working through Obsidian, apply the template with Templater. When writing
the file directly, resolve the template values before saving it:

- Set `title` and the H1 to the note's filename without `.md`.
- Set `created` to the current date in `YYYY-MM-DD` format.
- Preserve `type: note`, `tags: []`, and `state: draft` unless the user asks
  for different metadata.

Write the note to the path specified by the user. Do not invent a filing
folder when none was requested.
