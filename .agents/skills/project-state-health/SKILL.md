---
name: project-state-health
description: Report the state and health of a rendered AI-assistant repository. Use when asked for a health check, repository or vault status, counts of drafts or non-accepted knowledge, broken wikilinks or frontmatter, or validation that repository conventions remain in sync. Extend the small bundled scripts when the project gains new deterministic checks or status metrics.
title: Project state and health
type: skill
tags: [health, validation, wiki]
state: accepted
---

# Project state and health

Run every shell script in this skill's `scripts/` directory before reporting
that the rendered repository is healthy. It is intentionally a deterministic
local check: it does not modify files, access the network, or replace focused
tests for a changed component.

```sh
failed=0
for check in .agents/skills/project-state-health/scripts/*.sh; do
  printf '\n==> %s\n' "$check"
  bash "$check" || failed=1
done
exit "$failed"
```

Run these commands from the repository root. Each script owns one small,
explainable invariant and exits non-zero only when that invariant fails.

## Report the result

Start with the state report: total Markdown documents, accepted, draft,
archived, invalid or unclassified, and non-accepted totals. Then summarize
health failures before warnings. Do not claim the repository is healthy if a
check reports errors. Explain any intentional exception and either fix it or
record why it is being accepted.

## Extend it

Add a new, independently runnable shell script to
`.agents/skills/project-state-health/scripts/` as the rendered project gains
conventions. Keep every check small and explainable; it should print the
affected path and a concrete remedy. The loop above will discover new scripts
automatically. Update this skill and the project documentation when adding a
new required invariant.

Use a focused test in addition to these scripts for code such as the Wiki MCP;
the state and health check verifies repository-wide conventions, not component
behavior.
