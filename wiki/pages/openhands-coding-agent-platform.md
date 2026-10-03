---
title: "OpenHands Coding-Agent Platform"
type: research-report
tags: [openhands, coding-agents, orchestration, local-first, security]
state: accepted
created: 2026-09-13
sources:
  - "_raw/research/openhands-coding-agent-platform/report.md"
---

# OpenHands Coding-Agent Platform

## Conclusion

OpenHands is a capable local coding-agent execution platform and SDK, not a
complete deterministic delivery pipeline. Its best fit is as a replaceable,
sandboxed worker behind an existing deterministic task controller.

For the current cloud-first goal, defer OpenHands. Start with GitHub Agentic
Workflows and the available Copilot models; evaluate OpenHands later when a
local/private or provider-neutral worker solves a demonstrated need. See
[[deterministic-agent-coding-control-plane]].

For the existing Go task system, keep admission, task state, budgets,
cancellation and verification in Go. Give OpenHands one bounded task in one
disposable Git worktree, run it in a Docker-backed workspace, and accept only
a patch, branch or draft pull request as output.

## Capability boundary

OpenHands provides:

- A Python SDK and REST/WebSocket agent server.
- A code-oriented reasoning/tool loop with typed events and tools.
- Local, Docker and remote workspace abstractions.
- Bash, file, browser and MCP tooling.
- Provider-neutral LLM access and ACP-agent delegation, including Codex paths.
- Conversation persistence, sequential subagents and resumption.
- GitHub/event automations and pull-request workflows.
- OpenTelemetry traces for agent, model and tool activity.
- Risk analysis and confirmation hooks as defense in depth.

It does not inherently provide:

- Deterministic interpretation of natural-language tasks.
- A trustworthy authorization decision derived from issue/comment text.
- Guaranteed worker termination or credential revocation.
- Protected merge/deployment authority and final CI acceptance.

## Recommended composition

```text
Go task controller
  -> validate task contract
  -> create disposable worktree
  -> start bounded OpenHands Docker worker
  -> collect events, usage and diff
  -> terminate worker and revoke task credentials
  -> deterministic tests and path/diff policy
  -> draft PR -> human/protected merge
```

Avoid process mode for unattended work: it has no sandbox isolation and runs
with the macOS user's filesystem and command permissions. Docker is preferred,
but host mounts, network access and Docker-socket exposure remain trusted
boundaries.

## Alternatives

| Need | Better starting point |
| --- | --- |
| Smallest Codex-specific local worker | Direct Codex SDK/API behind Go |
| GitHub-native cloud policy and safe outputs | GitHub Agentic Workflows |
| Custom stateful agent application | LangGraph plus Deep Agents |
| Durable queues, timers and long approval waits | Temporal or cloud durable workflows |
| Persistent attended terminal sessions | [[herdr-coding-agent-runtime]] |

## Decision

Do not make OpenHands the first implementation. The fastest route to cloud
execution is GitHub Agentic Workflows with Copilot under normal GitHub review
and merge controls.

If a local/private execution requirement appears, trial OpenHands against
direct Codex using the same four bounded tasks. Adopt it only if Docker
workspace lifecycle, evidence, cancellation, provider portability and tracing
materially reduce Go-side implementation without widening host or credential
access.

Keep subagents, hosted automations, local LLMs, broad MCP access and a new fleet
UI outside the first trial.

## Open questions and contradictions

- Exact Go-to-agent-server contract and stable event schema require a prototype.
- ACP-backed Codex permission behavior must be tested inside the chosen sandbox.
- Conversation/trace retention and secret redaction need validation.
- OpenHands V1 and older application documentation overlap; pin the tested
  version and record any interface drift.

## Sources

- [[_raw/research/openhands-coding-agent-platform/report]]
