---
name: moc
description: Curate the rendered project's `MOC.md` when its repository map, core areas, responsibilities, sources of truth, capabilities, or important relationships need to be added, corrected, or reviewed. Use this skill whenever the user asks to update, audit, maintain, or explain the project map of context, including after a structural or capability change.
title: Kustos MOC curation
type: skill
tags: [moc, documentation, navigation]
state: accepted
---

# Kustos MOC curation

`MOC.md` is Kustos's concise semantic map. Keep it useful for
orientation: it explains where important things live, what they are for, and
how they relate. It complements `README.md`, `AGENTS.md`, and the filesystem;
it does not duplicate their detail.

## Curate the map

1. Read `MOC.md`, `README.md`, and `AGENTS.md`, then inspect the relevant
   paths before changing the map. Use repository facts, not assumptions.
2. Add or update a core-area entry when a top-level area, major entry point,
   workflow, capability, ownership boundary, or source of truth materially
   changes. Preserve the `moc:path` marker format for navigable paths.
3. Keep descriptions brief and outcome-oriented. Record an area once in the
   most useful section instead of repeating its implementation details.
4. Update the sources-of-truth table and relationships only when the change
   affects authority, lifecycle, data flow, or a meaningful dependency.
5. Do not modify the MOC for routine internal edits that leave the repository's
   orientation and responsibilities unchanged.

## Preserve accuracy

Do not invent paths, capabilities, ownership, or relationships. Remove or
revise stale entries only after confirming the relevant implementation or
documentation changed. Keep the standard frontmatter and update the MOC in the
same change as the structural or capability change it describes.

## Validate

After editing, confirm every referenced path exists, run the smallest relevant
documentation or health check, and review the rendered Markdown for clarity.
