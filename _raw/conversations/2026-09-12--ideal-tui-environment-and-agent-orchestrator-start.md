---
title: "Ideal TUI environment and Agent Orchestrator starting point"
type: raw-conversation
tags: [conversation, tui, coding-agents, agent-orchestrator, codex, claude-code, opencode, neovim, hunk]
origin: codex-conversation
created: 2026-09-12
---

# Ideal TUI environment and Agent Orchestrator starting point

## Initial question

How should the new TUI-first development environment be designed when the
current tmux-dev setup is only a reference point rather than a compatibility
constraint?

## Decisions

- The goal is an ideal new environment, not incremental preservation of
  tmux-dev. It may be completely replaced if the research supports that choice.
- **Agent Orchestrator (AO)** is the starting tool for the new journey and the
  first supervisor/core candidate to evaluate.
- The environment remains Codex-first but must be adjustable to Claude Code
  and OpenCode.
- Neovim, Hunk, a Markdown-reading experience, and a PR-review workflow remain
  required roles in the target composition; the research will determine their
  exact integration and whether each belongs inside or beside the supervisor.

## Open questions

- Can Agent Orchestrator own the required persistent runtime, fleet
  supervision, worktree, review, and recovery responsibilities without adding
  unacceptable configuration or network boundaries?
- Which components should remain independent tools rather than features of the
  supervisor?
- What is the right fallback architecture if Agent Orchestrator does not meet
  the operational or local-first requirements?

## Related Wiki pages

- [[herdr-coding-agent-runtime]]
- [[cli-tool-discovery-watchlist]]
