---
name: project-state
description: Report Kustos's current descriptive state, including foundation documentation and curated Wiki knowledge. Use when asked for repository or Wiki status, counts of accepted, draft, archived, or non-accepted documents, document-type totals, or uncommitted-path counts. This skill reports facts; use project-health separately to validate correctness and curation completeness.
title: Kustos state
type: skill
tags: [state, reporting, wiki]
state: accepted
---

# Kustos state

Run every script in this skill's `scripts/` directory from the repository root:

```sh
for report in .agents/skills/project-state/scripts/*.sh; do
  printf '\n==> %s\n' "$report"
  bash "$report"
done
```

Report the output as a compact Kustos inventory of foundation documentation and
curated Wiki knowledge. Project-local domain artifacts may have their own
schemas, so add a project-specific read-only report for their metrics. This
skill does not determine whether the reported state is correct, healthy, or
ready for curation. Run `project-health` when the user needs that judgment.

## Extend it

Add a small read-only script to `.agents/skills/project-state/scripts/` for a
new descriptive metric. Keep it non-failing unless the report itself cannot be
produced; correctness failures belong to `project-health`.
