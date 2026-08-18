---
name: project-health
description: Validate the health and curation completeness of a rendered AI-assistant repository. Use when asked for a health check, to verify that all raw files are ingested, accepted knowledge is indexed, research is ready, inbox notes are curated, or repository conventions remain valid. Run every bundled shell check and report concrete work still required.
title: Project health
type: skill
tags: [health, validation, curation, wiki]
state: accepted
---

# Project health

Run every shell script in this skill's `scripts/` directory before reporting
that the rendered repository is healthy:

```sh
failed=0
for check in .agents/skills/project-health/scripts/*.sh; do
  printf '\n==> %s\n' "$check"
  bash "$check" || failed=1
done
exit "$failed"
```

Run the commands from the repository root. The checks are read-only and each
owns one small, explainable invariant. They validate structure and frontmatter,
wikilinks and the active index, Raw-input curation coverage, accepted-page
indexing, research readiness, and legacy-layout migration.

## Report the result

List required work first: missing ingestion, unindexed accepted pages, Raw
inputs awaiting curation, or invalid repository conventions. Do not call the
repository healthy while any check exits non-zero. Use `project-state` when a
descriptive count is useful alongside the result.

## Extend it

Add a new independently runnable shell script to
`.agents/skills/project-health/scripts/` when the project gains a new
deterministic invariant. Each check should print the affected path and a
concrete remedy. The loop discovers new scripts automatically. Use focused
component tests in addition to these repository-wide checks.
