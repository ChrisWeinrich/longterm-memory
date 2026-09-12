---
title: "Deterministic Agent Coding Control Plane"
type: research-plan
tags: [research, coding-agents, github-actions, governance]
state: accepted
created: 2026-09-12
---

# Deterministic Agent Coding Control Plane

## Question

How can a small engineering organization start reliable, bounded coding-agent
work, supervise it in the cloud, and stop or contain an agent that behaves
unexpectedly?

## Decision and audience

Decision-ready architecture and rollout recommendation for an engineering owner
with Codex, GitHub Copilot, GitHub Actions, and access to multiple model APIs.

## Scope

GitHub-native and cloud-run patterns for task intake, agent execution,
verification, merge/deployment gates, budgets, auditability, cancellation,
credential isolation, and an independent overseer.

## Exclusions

Building a proprietary general-purpose agent platform, autonomous production
deployment, vendor price comparison, and legal compliance analysis.

## Success criteria

Distinguish deterministic automation from bounded agentic work; compare viable
control-plane options; recommend a minimal first implementation and staged
path; identify concrete kill switches and non-negotiable controls.
