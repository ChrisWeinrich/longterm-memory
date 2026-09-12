---
title: oh-my-hi upstream dashboard capability snapshot
type: external-note
tags:
- external
- oh-my-hi
- coding-agents
- dashboard
- configuration
- external-source
origin: wiki-mcp
received_at: '2026-09-12T13:15:26Z'
---

# oh-my-hi upstream dashboard capability snapshot

# oh-my-hi upstream dashboard capability snapshot

Source retrieved 2026-09-12: https://github.com/netil/oh-my-hi

The upstream README describes oh-my-hi (Oh My Harness Insights) as a local dashboard for Claude Code and Codex. It discovers each tool from its configuration directory, parses local configuration and usage transcripts, stores structure/usage data in JSON and local SQLite, and serves a dashboard on localhost (default port 8282).

Documented inventory categories: skills, agents, plugins, hooks, memory, MCP servers, rules, principles, commands, teams, and plans. It supports global and per-project scopes plus Claude Code/Codex side-by-side views. It also has usage, context-window, token-attribution, cost, cache, and session-replay analysis.

The documented scope is local Claude Code and Codex harness data. The README does not establish ChezMoi source ownership, template-to-target drift comparison, coverage of other agent ecosystems, or orchestration of live agent processes. Its local-only claim is documentation evidence rather than an independent source-code/privacy audit.

License: MIT. Upstream offers a Claude Code plugin path and a standalone npm CLI.
