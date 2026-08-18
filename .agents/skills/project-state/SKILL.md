---
name: project-state
description: Report the current descriptive state of a rendered AI-assistant repository. Use when asked for repository or vault status, counts of accepted, draft, archived, or non-accepted documents, document-type totals, or uncommitted-path counts. This skill reports facts; use project-health separately to validate correctness and curation completeness.
title: Project state
type: skill
tags: [state, reporting, wiki]
state: accepted
---

# Project state

Run every script in this skill's `scripts/` directory from the repository root:

```sh
for report in .agents/skills/project-state/scripts/*.sh; do
  printf '\n==> %s\n' "$report"
  bash "$report"
done
```

Report the output as a compact inventory. It describes the repository as it is;
it does not determine whether that state is correct, healthy, or ready for
curation. Run `project-health` when the user needs that judgment.

## Extend it

Add a small read-only script to `.agents/skills/project-state/scripts/` for a
new descriptive metric. Keep it non-failing unless the report itself cannot be
produced; correctness failures belong to `project-health`.
