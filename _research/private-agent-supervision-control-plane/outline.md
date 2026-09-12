---
title: "Private Codex and Claude Agent Supervision Control Plane"
type: research-plan
tags: [research, coding-agents, orchestration, terminal, tmux, codex, claude-code, mcp, chezmoi]
state: accepted
created: 2026-09-12
---

# Private Codex and Claude Agent Supervision Control Plane

## Question

Which ideal, TUI-first development environment should replace the current
workflow for supervising a high and growing multi-repository fleet of
persistent interactive agent sessions—Codex first, adjustable to Claude Code
and OpenCode—with Agent Orchestrator (AO) as the first core candidate?

## Decision and audience

Christian needs an evidence-backed target composition and a ranked core-runtime
recommendation before installing it. AO is the first tool to evaluate, not an
assumed winner. The report must identify an AO-first trial, a fallback, and a
strictly non-production validation plan. It is not approval to install, enable
integrations, expose a network service, or change ChezMoi.

## Scope

- Evaluate Agent Orchestrator (AO) first as the proposed core. Compare it with
  Agent Manager, Herdr, Agent Deck, NTM, and Paseo as fallback or superior-core
  candidates; assess cmux, CodexMonitor, Concord MCP, and ax only when they
  clarify the decision or are materially stronger alternatives.
- Verify official documentation, repositories, release/configuration files,
  and issue trackers as needed for macOS compatibility, Codex and Claude Code
  support, status detection, persistence/recovery, worktrees, review workflow,
  machine-readable control, and operational maturity.
- Evaluate fleet-scale navigation: grouping, filtering, and attention triage by
  repository, worktree, branch, agent, and session; identify documented limits
  or degradation risks when many sessions and repositories are active.
- Treat the existing tmux-dev runtime as a current-state reference only:
  per-project sessions and live Neovim/Hunk/agent panes show requirements, not
  constraints. Explicitly test whether AO can replace it completely, including
  persistence, attachment, worktrees, agent follow-ups, and recovery.
- Evaluate configuration/file mutation, MCP/skills/hooks/credentials handling,
  local sockets/listeners/plugins/relays/SSH/mobile surfaces, defaults,
  authentication, and declarative ChezMoi compatibility.
- Separate Hunk's review-first role from agent-supervision responsibilities;
  assess a suitable companion workflow. Include MCP Inspector CLI only as a
  read-only MCP-health companion.
- Assess the supporting TUI roles separately: Neovim for folder/file/code
  navigation, a Markdown reader compatible with an Obsidian-like reading
  experience, and a GitHub pull-request reviewer that can surface PR metadata,
  comments, and safe review actions. Do not assume that a local diff viewer is
  also a PR reviewer.
- Prefer Codex as the primary first-class agent, but verify that Claude Code and
  OpenCode can be selected per session without unmanaged global config changes.
- Consider credible additional terminal-native or tmux-compatible alternatives
  if official evidence shows they compete directly with the primary candidates.

## Exclusions

- No installation, configuration mutation, secret handling, network exposure,
  user-account changes, or live remote-machine setup.
- No recommendation based only on popularity, screenshots, or list inclusion.
- No claim that status detection is authoritative without documenting its
  mechanism and its failure modes.
- No one-shot swarm runner as the primary answer unless it demonstrably meets
  the persistent interactive-session requirements.
- Do not replace Neovim or introduce a large Neovim distribution without
  explicit evidence that the target architecture needs it.

## Success criteria

- A decision matrix answers all ten research criteria from the external brief,
  including every persistence event and every potential trust/config boundary.
- Each material claim has a primary source URL and date when available; unknown
  behavior is explicitly marked unknown.
- The recommendation determines whether AO can replace tmux-dev completely;
  if it cannot, it names the smallest compatible residual runtime rather than
  assuming tmux-dev must remain.
- A proposed component map assigns one clear owner for supervisor, persistent
  runtime, code/folder navigation, local diff review, PR review, and Markdown
  reading, with no unnecessary duplicate terminal or agent session managers.
- The AO-first trial is Codex-first and documents exactly how a user can switch
  an individual session to Claude Code or OpenCode.
- The report provides a no-install-yet test protocol across at least three
  repositories, multiple worktrees, and more than four mixed Codex/Claude
  sessions. It must exercise waiting/error conditions, terminal/UI and harness
  restarts, cross-repository follow-up prompts and triage, status verification,
  Hunk review, and an MCP Inspector read-only probe.

## Source brief

- [[_raw/external/2026-09-12--133523--research-brief-private-codex-claude-agent-supervision-control-plane]]
- [[_raw/conversations/2026-09-12--tui-first-agent-development-environment]]
- [[_raw/conversations/2026-09-12--ideal-tui-environment-and-agent-orchestrator-start]]
