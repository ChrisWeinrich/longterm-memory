---
title: "TUI-first agent development environment direction"
type: raw-conversation
tags: [conversation, tui, coding-agents, codex, claude-code, opencode, tmux, neovim, hunk, git]
origin: codex-conversation
created: 2026-09-12
---

# TUI-first agent development environment direction

## Initial question

How should the personal development environment evolve around a large,
multi-repository fleet of agent sessions while staying TUI-first and
Codex-centred?

## Consensus / current state

- The environment must supervise many concurrent sessions across multiple Git
  repositories, not only a small per-project set.
- The desired centre is an Agent Manager-like supervisor: Codex-first, but
  adjustable to Claude Code and OpenCode rather than limited to one provider.
- Neovim should remain the folder, file, and code-navigation layer.
- Hunk should be part of the agent-work review workflow as a dedicated diff
  viewer.
- A strong Markdown-reading experience and a GitHub pull-request review tool
  are required adjacent capabilities. The final split between an Obsidian-like
  reader and terminal tooling remains to be decided by evidence and usability.
- The existing runtime already uses per-project `tmux-dev` sessions and the
  current live sessions demonstrate dedicated Neovim, Hunk, Codex, and shell
  panes in several repositories.

## Open questions

- Which supervisor provides the right fleet view without replacing or fighting
  the existing tmux-dev runtime?
- Which PR reviewer supplies GitHub review context and comments that Hunk's
  local diff workflow does not own?
- Is the existing Neovim Markdown rendering sufficient, or should a separate
  terminal reader complement a retained graphical Markdown/Obsidian workflow?
- How should Codex-first behavior be made configurable for Claude Code and
  OpenCode without unmanaged global configuration mutation?

## Related Wiki pages

- [[herdr-coding-agent-runtime]]
- [[cli-tool-discovery-watchlist]]
