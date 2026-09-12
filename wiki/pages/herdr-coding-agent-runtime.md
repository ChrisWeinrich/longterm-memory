---
title: "Herdr: Coding-Agent Runtime"
type: research-report
tags: [herdr, coding-agents, terminals, orchestration, plugins]
state: accepted
created: 2026-09-12
sources:
  - "_raw/research/herdr-dev/report.md"
---

# Herdr: Coding-Agent Runtime

## Conclusion

Herdr is a persistent terminal runtime for existing coding-agent CLIs. It
keeps their real terminal panes running when the client detaches, shows agent
state across workspaces and machines, and supplies CLI and local-socket control
for agents, scripts, and plugins. It complements Kustos; it is not a knowledge
store or an agent replacement.

## Agent quick reference

| Start here | Official link |
| --- | --- |
| Help a human understand or set up Herdr | [Agent guide](https://herdr.dev/agent-guide.md) |
| All documentation | [Docs](https://herdr.dev/docs/) |
| Run an agent and detach/reattach | [Quick start](https://herdr.dev/docs/quick-start/) |
| Supported agents and status detection | [Agents](https://herdr.dev/docs/agents/) |
| Session and restart semantics | [Session state](https://herdr.dev/docs/session-state/) |
| SSH-connected machines | [Connecting machines](https://herdr.dev/docs/connecting-machines/) |
| CLI and local socket control | [Socket API](https://herdr.dev/docs/socket-api/) |
| Agent-specific configuration changes | [Integrations](https://herdr.dev/docs/integrations/) |
| Executable plugin model | [Plugins](https://herdr.dev/docs/plugins/) |

## Key points

- Use Herdr when multiple agents or projects should remain live while the human
  moves between terminals or machines.
- Detach preserves live processes. A server restart does not; Herdr restores
  layout and may restore screen history or a supported agent's native session.
- Codex, Claude Code, Copilot CLI, Cursor Agent CLI, and many others are
  detected, but state quality varies by integration and screen detection.
- The local socket API can read panes, send prompts, manage layout, and control
  integrations. Treat it as a trusted-local control boundary.
- SSH machines and plugins are operational extensions, not passive features:
  review access, configuration changes, and third-party code before use.

## Open questions and contradictions

- Any Codex/Claude integration should be reconciled with ChezMoi ownership
  before installation.
- Herdr's fit alongside `tmux-dev` should be tested in an isolated project
  before changing the established terminal workflow.

## Sources

- [[_raw/research/herdr-dev/report]]
