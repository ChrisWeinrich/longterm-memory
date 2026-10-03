---
title: "Deterministic Agent Coding Control Plane"
type: research-report
tags: [coding-agents, github-actions, github-copilot, codex, cloud, governance]
state: accepted
created: 2026-09-13
sources:
  - "_raw/research/deterministic-agent-coding-control-plane/report.md"
  - "_raw/research/deterministic-agent-coding-control-plane--alternatives-2026-09-13/report.md"
  - "_raw/research/deterministic-agent-coding-control-plane--deep-2026-09-13/report.md"
---

# Deterministic Agent Coding Control Plane

## Conclusion

A coding agent is probabilistic. Determinism belongs in the control plane
around it: admission, permissions, resource limits, required evidence,
verification, merge/deployment gates and cancellation.

The accepted first implementation is **GitHub Agentic Workflows with the
Copilot engine**, using the models already available through GitHub Copilot.
This is the shortest route to cloud execution and keeps task, run, pull-request
and review state in GitHub. Compare Codex later under the same task contract;
do not build a custom orchestrator before a concrete GitHub-native limitation
appears.

## Target flow

```text
maintainer dispatch / admitted issue
  -> deterministic task-policy check
  -> one bounded cloud-agent run
  -> draft pull request only
  -> deterministic CI and diff/path policy
  -> CODEOWNER or human review
  -> protected merge queue
  -> separate post-merge deployment gate
```

Only the bounded implementation step is agentic. Every authority-bearing
transition is ordinary code or GitHub policy.

## Initial task contract

Require an explicit goal, acceptance checks, risk class, allowed and forbidden
paths, allowed commands, dependency/network policy, file/diff ceiling, run
budget and expected draft-PR output.

Start only with documentation, isolated tests, lint/type corrections and small
local refactors. Exclude authentication, permissions, secrets, workflows,
infrastructure, production configuration, destructive migrations and
dependency upgrades.

## First rollout

1. Protect the default branch with required CI and human/CODEOWNER review.
2. Create one manually dispatched Agentic Workflow using Copilot.
3. Permit only a draft pull request as safe output.
4. Set explicit tools, repository permissions, network policy, duration and
   AI-credit limits.
5. Run four low-risk tasks and record cost, duration, changed paths, CI result,
   review rework, policy violations and cancel latency.
6. Add label-driven admission only after the manual baseline is reliable.

## Alternatives and escalation path

| Demonstrated need | Next option |
| --- | --- |
| Existing Copilot cloud models are sufficient | Keep GitHub Agentic Workflows |
| Fair comparison with OpenAI Codex | Change engine under the same task contract |
| GitHub cannot express task schema or provider routing | Small Actions wrapper plus Codex SDK/API |
| Private/local isolated execution | [[openhands-coding-agent-platform]] |
| Persistent attended terminal agents | [[herdr-coding-agent-runtime]] |
| Long approvals, cross-repository queues or private-network workers | Durable cloud workflow service |
| A stateful agent service is itself the product | LangGraph/LangSmith evaluation |

## Non-negotiable controls

- The agent cannot merge or deploy.
- No production secret or broad cloud credential enters its runtime.
- No privileged run starts from arbitrary comments, PR text or fork code.
- Required checks and protected branches have no agent bypass.
- Cancellation is paired with stopping new admissions and revoking external
  worker credentials.
- A model reviewer is advisory and never replaces deterministic checks or a
  human approval.

## Open questions and contradictions

- Verify Agentic Workflow, model and billing availability in the target GitHub
  organization before implementation.
- Define the first repository's exact path/command policy and four pilot tasks.
- Set the monthly budget and per-run time/credit limits.
- Copilot model availability and a separate `claude` workflow engine are not
  equivalent; confirm whether the intended Claude access is a Copilot model
  choice or separately authenticated engine before configuration.

## Sources

- [[_raw/research/deterministic-agent-coding-control-plane/report]]
- [[_raw/research/deterministic-agent-coding-control-plane--alternatives-2026-09-13/report]]
- [[_raw/research/deterministic-agent-coding-control-plane--deep-2026-09-13/report]]
