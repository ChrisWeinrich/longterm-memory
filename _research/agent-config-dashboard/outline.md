---
title: "Agent and Configuration Dashboard — Research Plan"
type: research-plan
tags: [research, agents, configuration, mcp, skills, chezmoi, dashboard]
state: accepted
created: 2026-09-12
---

# Agent and Configuration Dashboard

## Question

Which existing tools or lightweight local components provide the most useful,
private overview of coding agents, skills, MCP servers, policies, effective
configuration, and source-versus-live drift between the ChezMoi source and
this Mac?

## Decision and audience

Decision support for Christian: whether to adopt an existing tool, combine
specialized tools, or build a small read-only collector and viewer.

## Scope

- Current open-source and commercial dashboards, inspectors, IDE extensions,
  and Dotfiles-/ChezMoi-adjacent viewers for Claude Code, Codex, Copilot,
  Cursor, and comparable coding agents.
- Visibility into skills, MCP servers, instructions, policies, permissions,
  and effective runtime configuration.
- Local or offline-capable operation, network exposure, secret redaction,
  licensing, maintenance, and ChezMoi integration.
- MCP Inspector and redacted JSON/diff viewers as individual components, not
  as assumed complete solutions.
- A gap analysis for a small, read-only source-versus-live collector that
  excludes secrets unambiguously.

## Exclusions

- Do not build, install, or deploy a dashboard.
- Do not collect, store, or send secrets, tokens, or complete private
  configuration contents to external services.
- Do not change ChezMoi, agent, or MCP configuration.
- Do not assess general chat UIs unless they make a concrete contribution to
  agent or configuration inventory.

## Success criteria

The Raw report contains an evidenced comparison matrix, separates facts from
inference, records official URLs and retrieval dates, assesses local privacy
and redaction, covers ChezMoi source-versus-live comparison, and makes a
reasoned recommendation with explicit gaps for a possible read-only custom
implementation.
