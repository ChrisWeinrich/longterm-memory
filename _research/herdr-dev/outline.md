---
title: "Herdr — Research Plan"
type: research-plan
tags: [research, herdr, coding-agents, terminals, orchestration, plugins]
state: accepted
created: 2026-09-12
---

# Herdr

## Question

What can Herdr from `herdr.dev` do for coding agents, which capabilities and
operational boundaries matter for this Mac, and what concise, official
reference should Kustos provide to agents?

## Decision and audience

Practical reference for Christian and his coding agents. It should support a
later decision about adopting Herdr as a persistent terminal runtime for
agents; it is not approval to install, configure, or expose it.

## Scope

- Herdr's role as a terminal runtime and multiplexer for existing coding-agent
  CLIs, rather than an agent wrapper or replacement.
- Persistent sessions and layouts; detach, reconnect, restart restoration,
  history replay, and native agent-resume behavior.
- Agent detection and status, local and SSH-connected machines, the CLI and
  local socket API, supported-agent integrations, and workflow plugins.
- Supported platforms, installation and update paths, configuration,
  networking and SSH boundaries, licensing, release maturity, and security
  implications for a private Mac setup.
- A compact agent-facing guide with direct official links, especially
  `https://herdr.dev/agent-guide.md`, `https://herdr.dev/docs/`, the API,
  configuration, remote-machine, and plugin documentation.

## Exclusions

- Do not install, activate, configure, or expose Herdr on this Mac.
- Do not grant it secrets, credentials, remote-host access, or an agent's
  existing terminal sessions.
- Do not evaluate unrelated PHP product "Herd" or general agent frameworks.
- Do not recommend unreviewed community plugins without separately assessing
  their source and permissions.

## Success criteria

The Raw report contains a sourced capability map, direct official links,
facts clearly separated from inference, platform and security caveats, and a
short agent-oriented reference covering when to use Herdr, when not to, and
which documentation to read first.
