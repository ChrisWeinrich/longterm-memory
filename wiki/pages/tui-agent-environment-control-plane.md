---
title: "TUI Agent Environment Control Plane"
type: research-report
tags: [coding-agents, orchestration, tui, codex, claude-code, opencode, neovim, hunk, github]
state: accepted
created: 2026-09-12
sources:
  - "_raw/research/private-agent-supervision-control-plane/report.md"
  - "_raw/external/2026-09-12--133523--research-brief-private-codex-claude-agent-supervision-control-plane.md"
  - "_raw/conversations/2026-09-12--tui-first-agent-development-environment.md"
  - "_raw/conversations/2026-09-12--ideal-tui-environment-and-agent-orchestrator-start.md"
---

# TUI Agent Environment Control Plane

## Conclusion

Trial **Agent Orchestrator (AO)** first as the local fleet-supervision and
lifecycle layer for a multi-repository, Codex-first environment. AO is a
desktop-local control plane rather than a TUI terminal replacement; keep
Neovim for code navigation and Hunk for local diff review. A successful AO
trial would replace the current tmux-dev responsibility deliberately, not
merge two competing terminal runtimes.

Use **Agent Manager** as the fallback if AO fails its local-only, telemetry,
configuration-ownership, or recovery acceptance gates. Agent Manager is more
terminal-native and preserves installed CLI configuration, but its status is
primarily heuristic terminal-screen matching.

## Target composition

| Responsibility | Preferred owner | Boundary |
| --- | --- | --- |
| Fleet supervision, worktrees, task lifecycle, CI/PR feedback | Agent Orchestrator, after trial | Local desktop/daemon control plane; validate listener, telemetry, and filesystem effects first |
| Agent runtime | AO native-terminal worker; Agent Manager tmux server if AO is rejected | Do not retain a second generic runtime without a defined role |
| Folder, file, and code navigation | Existing Neovim | Keep the lean viewer-first configuration |
| Local review of agent changes | Hunk in the selected worktree | Local diff review is distinct from PR review |
| Pull-request review | AO's worker/PR loop, or GitHub CLI/browser plus the owning agent | Hunk does not fetch or submit GitHub review state |
| Markdown reading | Obsidian for the knowledge vault; terminal reader only if separately selected | No researched TUI matches the Obsidian-like knowledge-reading role |
| Read-only MCP health | MCP Inspector CLI with an explicit config | Probe with `initialize` and `tools/list`; do not write configuration |

## Guardrails

- ChezMoi remains the sole owner of global agent configuration, MCP entries,
  skills, hooks, launchers, and guidance.
- Reject a trial that silently writes `~/.codex`, `~/.claude`, shared MCP files,
  or ChezMoi-managed paths.
- Require loopback or Unix-socket local control only; no public listener,
  remote relay, mobile pairing, or unreviewed plugin.
- Treat status as attention triage until the tool proves its handling of
  waiting, approval-blocked, and error states on the installed agent versions.

## First trial and fallback

Run AO only in a disposable repository with temporary/reviewable support paths
when supported. Exercise mixed Codex and Claude Code workers across worktrees,
then an optional OpenCode worker; verify state accuracy, follow-up routing,
restart recovery, listener ownership, and cleanup. Use `hunk diff --watch` for
the local review surface. If any acceptance gate fails, stop and run the same
experiment with Agent Manager.

## Related knowledge

- [[herdr-coding-agent-runtime]] — Herdr remains a capable runtime, but its
  integration hooks are an ownership concern for this first trial.
- [[cli-tool-discovery-watchlist]] — source list for subsequent TUI tool
  evaluation.

## Open questions and contradictions

- AO's exact first-launch state/config paths, listener authentication,
  telemetry opt-out, and complete configuration-mutation behavior require an
  isolated local test.
- AO recovery across macOS sleep, reboot, and SSH disconnect is not yet proven.
- A terminal Markdown reader and a dedicated PR-review client remain separate
  choices once the supervision core is validated.

## Sources

- [[_raw/research/private-agent-supervision-control-plane/report]]
