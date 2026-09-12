---
title: 'Research brief: private Codex + Claude agent supervision control plane'
type: external-note
tags:
- external
- coding-agents
- orchestration
- terminal
- tmux
- codex
- claude-code
- mcp
- chezmoi
- research
origin: wiki-mcp
received_at: '2026-09-12T13:35:23Z'
---

# Research brief: private Codex + Claude agent supervision control plane

## Decision to research

Select a durable, private, local-first control plane for supervising all interactive **Codex** and **Claude Code** sessions on the personal Mac.

The intended outcome is one reliable place to see active agents, their state (working / waiting / idle / failed), working directory or worktree, and attention needed; switch or send a follow-up promptly; preserve or reliably resume sessions; and review work safely. It must not be merely a one-shot swarm runner.

## Environment and non-negotiable constraints

- Personal macOS; existing workflow uses `tmux-dev` and `tmux-bridge`.
- ChezMoi (`/Users/christianweinrich/.local/share/chezmoi`) is the source of truth for durable Codex, Claude, Copilot, shared skills, MCP entries, launchers, and agent guidance.
- A candidate must not silently mutate `~/.codex`, `~/.claude`, global MCP registration, skills, credentials, or project configuration. If it supports such actions, determine whether they can be disabled or managed declaratively through ChezMoi.
- Private/local-first operation is strongly preferred. No public web binding. Any socket/API, remote control, phone control, relay, SSH, or plugin must be evaluated as a trust boundary. Tailscale-only access is acceptable only if explicitly needed.
- Preserve the ability to run both Codex and Claude Code; do not assume a single provider.
- MCP configuration health and config drift monitoring are a desired adjacent capability, but need not be owned by the agent-session manager. The official MCP Inspector CLI is a potential read-only companion.
- Hunk is a complementary review-first terminal diff viewer, not an agent manager; assess the best integration workflow but do not categorize it as a harness.

## Candidates already discovered

### Strong candidates to compare deeply

1. **Agent Manager** — Go/tmux TUI. Persistent private tmux server, Codex and Claude support, live status, quick prompts without attach, project grouping, worktrees, session fork/revive, and interactive diff review with comments returned to agent.
   - Repository: https://github.com/YoanWai/agent-manager
   - Important claim to validate: it launches each installed CLI as-is, retaining its login, config files, and MCP servers.
   - Important risk: its own config/state location and optional MCP integration must remain compatible with ChezMoi ownership.

2. **Herdr** — persistent terminal runtime/multiplexer owning real PTYs. Detach/reattach, agent status, worktrees, local CLI/socket API, event subscriptions, Codex resume support after restart.
   - Docs: https://herdr.dev/docs/
   - Repository/documentation area: local socket API and session state.
   - Important difference: it owns the terminal runtime rather than layering on tmux. Server restart normally stops processes; it may restore layout and resume native agent sessions.
   - Important risk: integration/plugin/sockets are trusted-local control boundaries; determine fit or conflict with tmux-dev.

3. **Agent Deck** — tmux-based fleet TUI with status, groups, worktrees, session forking, cost dashboard, MCP and skill manager, optional localhost web UI.
   - Repository: https://github.com/asheshgoplani/agent-deck
   - Important risk: it can attach/toggle MCPs and skills and manage agent config. Determine if safe read-only/disabled modes exist and whether it duplicates ChezMoi-managed state.

4. **NTM (Named Tmux Manager)** — broader tmux control plane: agent sessions, messaging, file reservations, worktrees, approvals/policy, checkpoints/audit trails, robot JSON, local REST/SSE/WebSocket.
   - Repository: https://github.com/Dicklesworthstone/ntm
   - Important risk: potentially much more opinionated/integration-heavy than required; evaluate API binding/authentication and interaction with existing tmux-dev.

5. **Paseo** — self-hosted daemon with CLI/API and desktop/web/mobile clients; runs Codex, Claude, Copilot, OpenCode, Pi in parallel, supports worktrees and remote host control.
   - Repository: https://github.com/getpaseo/paseo
   - Important risk: daemon, optional encrypted relay, networking, plugins, and remote/mobile surfaces may add unnecessary operational/security scope. Evaluate strict local-only mode.

### Secondary candidates / adjacent tools

- **Agent Orchestrator (AO)**: desktop lifecycle control plane that couples task, worktree/branch, agent, diff, PR, CI, review, and merge. https://github.com/Untrivial-ai/agent-orchestrator
- **cmux**: native macOS Ghostty-based terminal with notifications, workspace metadata, SSH, CLI/socket control; a cockpit, not necessarily process persistence comparable with Herdr. https://github.com/manaflow-ai/cmux
- **CodexMonitor**: Codex-specific GUI using app-server; less suitable for Claude supervision. https://github.com/Dimillian/CodexMonitor
- **Concord MCP**: local-first agent-to-agent communication, task handoff, and file-claim collision detection across Codex/Claude. It writes client config by default, so evaluate `--no-mcp`/manual registration only. https://github.com/Get-Concord-AI/concord-mcp
- **ax**: local-first observability and retrospective learning over Codex/Claude transcripts; a complement, not live session supervisor. https://github.com/Necmttn/ax
- **MCP Inspector CLI**: read-only MCP probing (`initialize`, `tools/list`, resources/prompts) from supplied config, complementing any selected harness. https://github.com/modelcontextprotocol/inspector
- **Hunk**: review-first terminal diff viewer; `hunk diff --watch` and its skill can support a review workflow beside the harness. https://github.com/modem-dev/hunk

## Research questions / decision criteria

1. Which tool is best for 2–10 persistent interactive Codex + Claude sessions on macOS, today?
2. How exactly do each candidate detect status for Codex and Claude? What breaks after upstream CLI UI/output changes?
3. What survives terminal close, tool UI close, daemon/server restart, Mac sleep/reboot, and network/SSH disconnect?
4. Does it integrate with or replace tmux? Can it coexist safely with tmux-dev and tmux-bridge?
5. How do it create, locate, clean up, and protect git worktrees? What is its recovery story?
6. What configuration, MCP, skill, hooks, credentials, environment, or repository files can it mutate? Can that behavior be switched off? What must be modeled in ChezMoi?
7. What local/network APIs, listeners, socket files, plugins, relays, or remote-control mechanisms are exposed? Bind defaults, authentication, encryption, capabilities, and secrets must be explicit.
8. Can it provide machine-readable status to a future small read-only ChezMoi-owned monitor? Assess CLI JSON, socket, REST/SSE/WebSocket APIs and stability.
9. Is Hunk best used in an auxiliary terminal pane, through the harness’s built-in diff review, or via another integration?
10. Search for credible additional alternatives not listed above, especially terminal-native/tmux-compatible tools, then explain why they are better/worse rather than just listing them.

## Deliverable

Produce a deep, evidence-backed comparison and a short ranked recommendation. Include an explicit **do-not-install-yet** testing plan in a throwaway repository: two Codex + two Claude sessions, two worktrees, intentionally waiting/error states, terminal/UI restart, harness restart, prompt-follow-up, status accuracy, isolated diff review with Hunk, and MCP Inspector read-only probe. Recommend a single first trial candidate plus a fallback; only then propose ChezMoi integration.
