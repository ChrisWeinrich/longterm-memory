---
title: "Herdr: Coding-Agent Runtime — Deep-Research Report"
type: raw-research-report
tags: [research, herdr, coding-agents, terminals, orchestration, plugins]
origin: research-workflow
created: 2026-09-12
---

# Herdr: Coding-Agent Runtime

## Conclusion

**Herdr is a persistent terminal runtime and multiplexer for existing coding
agent CLIs.** It does not replace Codex, Claude Code, Copilot CLI, Cursor
Agent CLI, or other agents: it gives each one a real terminal pane, keeps that
pane running in a background server after the client detaches, and surfaces
agent state across workspaces and machines.

It is relevant when several agents or projects need to keep running while the
human moves between terminals or machines. It is not merely a dashboard: its
CLI and local socket API can create and control workspaces, panes, agents, and
plugins. That power makes it an operational runtime, so installation,
integrations, SSH machines, and community plugins require deliberate review.

## Agent quick reference

| Need | Official reference |
| --- | --- |
| Ask an agent to explain, set up, or troubleshoot Herdr | [Agent guide](https://herdr.dev/agent-guide.md) |
| Documentation entry point | [Herdr docs](https://herdr.dev/docs/) |
| Start a local session and detach/reattach | [Quick start](https://herdr.dev/docs/quick-start/) |
| Supported agents, detection, status, and direct attach | [Agents](https://herdr.dev/docs/agents/) |
| Per-agent configuration changes, including Codex and Claude Code | [Integrations](https://herdr.dev/docs/integrations/) |
| What survives detach, restart, restore, and handoff | [Session state and restore](https://herdr.dev/docs/session-state/) |
| Saved SSH machines and remote-operation limits | [Connecting machines](https://herdr.dev/docs/connecting-machines/) |
| CLI and local socket control surface | [Socket API](https://herdr.dev/docs/socket-api/) |
| Settings and configuration reference | [Configuration](https://herdr.dev/docs/configuration/) |
| Plugin model and trust boundaries | [Plugins](https://herdr.dev/docs/plugins/) |
| Source, issue tracker, and Apache-2.0 license | [GitHub repository](https://github.com/herdrdev/herdr) |

## Evidence

### What it manages

- A Herdr session is a background server namespace containing workspaces,
  tabs, panes, agents, and local state. Starting `herdr` attaches to the
  default background session; detaching or closing the terminal leaves its
  agent processes running. [Quick start](https://herdr.dev/docs/quick-start/)
- It detects common agent CLIs, including Claude Code, Codex, GitHub Copilot
  CLI, Cursor Agent CLI, OpenCode, Hermes Agent, and others. Each agent stays
  in its terminal with its shell, prompts, logs, and processes intact; Herdr
  reports working, blocked, done, or idle state in the sidebar. [Agents](https://herdr.dev/docs/agents/)
- Detection is not a universal guarantee. For many agents it reads the
  foreground process and terminal-screen patterns; direct integrations can
  supply session identity or lifecycle data. New or unusual prompts can appear
  idle rather than blocked until their detection rules cover that UI. [Agents](https://herdr.dev/docs/agents/)

### Persistence and recovery

| Event | Original processes continue? | What Herdr can restore |
| --- | --- | --- |
| Detach and reattach | Yes | Live layout, terminal state, and agent conversation, because the process remains alive |
| Server restart | No | Layout; optionally pane screen history; native agent conversation only where a supported session reference exists |
| Remote-network loss | Remote processes remain on their own machine | Cached state is shown until a fresh SSH connection arrives |

This distinction matters: Herdr is valuable for unattended agent work during a
client disconnect, but it is not a process checkpointing system across server
or machine restart. [Session state and restore](https://herdr.dev/docs/session-state/)

### Control and automation

- The CLI and local socket API share a control surface. They can inspect and
  manage workspaces, tabs and panes; read pane output; start, prompt, wait for,
  or attach to agents; reload configuration; manage integrations; and invoke
  plugins. The raw API uses newline-delimited JSON over a Unix-domain socket on
  Unix and a named pipe on Windows. [Socket API](https://herdr.dev/docs/socket-api/)
- Herdr ships a reusable in-pane agent skill. It is for an agent already inside
  a Herdr-managed pane and can inspect the layout, read output, split panes,
  and wait for work. The public `agent-guide.md` instead teaches an agent how
  to help a human learn or troubleshoot Herdr. [Agent skill file](https://herdr.dev/docs/agent-skill/)
- For Codex, Herdr documents an optional integration that writes a hook script,
  updates `hooks.json`, and enables the hooks feature in the Codex config. This
  is a configuration change, not passive observation. [Integrations](https://herdr.dev/docs/integrations/)

### Remote machines and plugins

- Herdr can combine Local and saved SSH machines in one client window. Each
  remote machine retains its own server, sessions, and processes; loss of one
  connection does not stop the others. [Connecting machines](https://herdr.dev/docs/connecting-machines/)
- Remote machines require ordinary SSH access. Multi-machine management is
  documented for macOS and Linux clients to macOS/Linux servers; Windows has
  stated limitations. Adding a machine may propose install, update, or server
  replacement, and the documented default is not to proceed without approval.
  [Connecting machines](https://herdr.dev/docs/connecting-machines/)
- Plugins are executable workflow packages with actions and event hooks. The
  public marketplace discovers GitHub repositories and explicitly says its
  listings are not reviewed; treat every third-party plugin as code to review.
  [Plugins](https://herdr.dev/docs/plugins/)

### Distribution and maturity

Herdr presents installers for macOS, Linux, and Windows, plus Homebrew, Nix,
and manual paths. Its public source repository is Apache-2.0 licensed. Product
features, integration behavior, detection manifests, and plugin listings are
fast-moving; verify them against the installed version before operational use.
[Herdr home](https://herdr.dev/) · [GitHub repository](https://github.com/herdrdev/herdr)

## Trade-offs and risks

- **Broad control surface:** A local socket API that can send agent prompts,
  read panes, and manage integrations should be reachable only by trusted local
  processes. Do not expose it as a generic network service.
- **Agent-state accuracy:** Screen-based status is useful for orientation, not
  a proof that an agent has completed safely. Treat `blocked`, `idle`, and
  `done` as operational signals that may need human verification.
- **Configuration mutation:** Optional integrations modify agent-specific
  configuration. Review their exact install/uninstall behavior and preserve
  ChezMoi ownership before enabling them.
- **Remote-machine access:** Saved SSH machines add a real remote-control
  boundary. Use existing, least-privilege SSH access and do not assume a
  background connection can answer authentication or approval prompts.
- **Plugin trust:** Community marketplace discovery is not review or security
  assurance. Prefer no plugins initially; inspect source and manifests before
  installation.

## Recommendation

Treat Herdr as a candidate **runtime layer**, complementary to Kustos rather
than a knowledge system. Start with the agent guide and quick start only after
deciding to evaluate it. Before enabling a Codex integration, SSH machine, or
plugin, inspect its documented filesystem and access effects and decide how it
fits the ChezMoi-managed configuration model.

For agents that only need reference material, provide the quick-reference links
above. For an agent actually running inside Herdr, use Herdr's own agent skill
and its local CLI/socket boundary—not unreviewed terminal automation.

## Open questions

- Does Herdr fit the existing `tmux-dev` workflow, or would it replace a
  currently preferred terminal-management boundary?
- Which integrations, if any, can be made ChezMoi-managed without conflicting
  with Codex, Claude, and Copilot configuration ownership?
- Is SSH machine aggregation useful enough to justify a new persistent remote
  access surface on this Mac?
- Should Herdr's agent skill be installed globally, or only after a local,
  isolated evaluation?

## Sources

All sources were retrieved on 2026-09-12. Product capabilities, versions,
integration behavior, and marketplace content should be rechecked before
installation or rollout.

- [Herdr home](https://herdr.dev/)
- [Herdr documentation](https://herdr.dev/docs/)
- [Quick start](https://herdr.dev/docs/quick-start/)
- [Agents](https://herdr.dev/docs/agents/)
- [Session state and restore](https://herdr.dev/docs/session-state/)
- [Connecting machines](https://herdr.dev/docs/connecting-machines/)
- [Socket API](https://herdr.dev/docs/socket-api/)
- [Integrations](https://herdr.dev/docs/integrations/)
- [Agent skill file](https://herdr.dev/docs/agent-skill/)
- [Plugins](https://herdr.dev/docs/plugins/)
- [Herdr GitHub repository](https://github.com/herdrdev/herdr)
