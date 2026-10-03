---
title: "Deterministic Agent Coding Control Plane query"
type: research-query
tags: [research, coding-agents, github-actions, governance]
state: accepted
created: 2026-09-12
---

# Deep research query

Research how an engineering team can safely initiate deterministic coding flows
with cloud coding agents. Compare GitHub Copilot coding agent and Agentic
Workflows, OpenAI Codex, plain GitHub Actions plus model APIs, and self-hosted
or third-party orchestrators where relevant. Establish practical control and
oversight patterns: constrained task contracts, ephemeral execution, least
privilege, validation, PR and deployment gates, observability, cost limits,
cancellation, circuit breakers, and independent review.

Use the accepted outline as the scope. Prefer original and official sources,
then peer-reviewed research, then reputable secondary analysis for context.
Record source URLs, publication dates when available, evidence, uncertainty,
and any inference separately from sourced facts.

## 2026-09-13 extension: execution alternatives

Compare the smallest viable deterministic shells for the existing GitHub
Copilot cloud-agent subscription and OpenAI/Codex API access. In particular,
separate GitHub Agentic Workflows with selectable engines from a custom
GitHub-Actions wrapper, and assess when a durable orchestrator (Temporal,
Azure Durable Functions, or LangGraph) is justified. State plainly which
options are an execution engine only rather than a control plane.

Write the completed report to
`_raw/research/deterministic-agent-coding-control-plane/report.md` from
`_templates/raw-research-report.md`. It is Raw material without a state and is
curated into `wiki/pages/` later.
