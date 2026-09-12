---
title: "Private Codex and Claude Agent Supervision Control Plane query"
type: research-query
tags: [research, coding-agents, orchestration, terminal, tmux, codex, claude-code, mcp, chezmoi]
state: accepted
created: 2026-09-12
---

# Deep research query

Research this question: Which ideal, TUI-first development environment should
replace the current workflow for supervising a high and growing multi-repository
fleet of persistent interactive agent sessions—Codex first, adjustable to
Claude Code and OpenCode—with Agent Orchestrator (AO) as the first core
candidate and without undermining Neovim, Hunk, or ChezMoi configuration
ownership?

Use the accepted outline as the scope. Prefer each candidate's official
documentation, source repository, release notes, configuration reference, and
security/network documentation; use issue trackers to verify edge cases and
limitations. Then consult Hunk and MCP Inspector official documentation only
for their complementary workflows.

For every candidate, determine: agent coverage and status-detection mechanism;
terminal/UI close, process/server restart, sleep/reboot, and SSH-disconnect
semantics; tmux relation; worktree lifecycle; all configuration and filesystem
mutations; API/socket/listener/plugin/relay boundaries; local-only defaults and
authentication; structured status/automation surface; and evidence of macOS
operation. Specifically assess grouping, filtering, attention triage, and
navigation across repositories, worktrees, branches, agent types, and many
simultaneous sessions; name documented limits or unknown scale behavior.
Clearly distinguish upstream claims from inferences and missing evidence.

Start with AO: verify its documented architecture, macOS support, actual agent
coverage, persistence/recovery model, worktree and PR lifecycle, status model,
local/network control surfaces, and every configuration mutation. Test whether
it can replace tmux-dev rather than merely coexist with it. Treat the current
tmux-dev layout only as evidence of required roles, not an invariant.

Treat the environment as composable rather than assuming one monolithic
application must own everything. Establish a responsibility map for: the
selected persistent runtime; fleet supervision; Neovim folder/file/code
navigation; Hunk local diff review; Markdown reading; and GitHub pull-request
review.
For Markdown and PR-review candidates, prefer official docs and verify terminal
operation, macOS compatibility, authentication/configuration impact, GitHub API
scope, local-only behavior, and how review comments or requested changes return
to the owning agent. Explain what remains a human GUI/Obsidian task if a TUI
does not meet the requirement.

Require Codex as the primary first-class session type, then verify explicit
per-session selection or adapters for Claude Code and OpenCode. Reject designs
that achieve multi-agent support by silently rewriting global agent, MCP,
skills, hooks, provider, or credential configuration outside ChezMoi.

Produce a comparison matrix, a ranked recommendation, a rejection rationale
for unsuitable candidates, and a no-install-yet test protocol. Include source
URLs, publication/release dates where available, uncertainty, and direct
answers to the source brief's ten questions.

Write the completed report to
`_raw/research/private-agent-supervision-control-plane/report.md` from
`_templates/raw-research-report.md`. It is Raw material without a state and is
curated into `wiki/pages/` later.
