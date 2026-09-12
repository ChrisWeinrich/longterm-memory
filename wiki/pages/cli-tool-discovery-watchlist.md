---
title: "CLI Tool Discovery Watchlist"
type: research-report
tags: [cli, terminal, tool-discovery, coding-agents, tui]
state: accepted
created: 2026-09-12
sources:
  - "_raw/research/cli-tool-discovery--shallow/report.md"
---

# CLI Tool Discovery Watchlist

## Conclusion

Use this short watchlist when searching for new command-line tools. It divides
the discovery job between broad CLI/TUI catalogues, modern Unix replacements,
and coding-agent tooling. The links are discovery sources, not a blanket
recommendation to install listed projects.

## Discovery pages

| When looking for | Start with | Why |
| --- | --- | --- |
| A CLI or TUI by domain | [Terminal Trove](https://terminaltrove.com/categories/) | Category-led discovery across developer, system, and terminal topics |
| A better modern replacement for a familiar command | [Awesome Modern CLI](https://github.com/thegdsks/awesome-modern-cli) | Maps classic command-line workflows to focused replacements |
| A broad catalogue of CLI apps | [Awesome CLI Apps](https://github.com/agarrharr/awesome-cli-apps) | Evergreen directory for deeper lookup |
| Coding agents, runtimes, worktrees, or orchestration | [Awesome CLI Coding Agents](https://github.com/bradAGI/awesome-cli-coding-agents) | Agent CLIs plus runners, sandboxes, and infrastructure |
| Newly appearing, uncurated projects | [GitHub CLI topic](https://github.com/topics/cli), [terminal topic](https://github.com/topics/terminal), [cli-agent topic](https://github.com/topics/cli-agent) | Sort by recently updated; verify projects independently |

## Suggested review routine

Review Terminal Trove, Awesome Modern CLI, and Awesome CLI Coding Agents about
every two weeks. Select at most three candidates, then evaluate each against
the existing shell, tmux-dev, MCP, and ChezMoi configuration boundaries before
installing it.

## Known candidates

- [[herdr-coding-agent-runtime]] is accepted knowledge for the persistent
  agent-runtime category.
- **Hunk** is a candidate review tool, not yet separately evaluated in this
  Wiki: [official repository](https://github.com/modem-dev/hunk).

## Open questions and contradictions

- Discovery-list inclusion does not establish project quality, safety, or
  compatibility with this environment.
- Configuration managers and provider switchers deserve extra review because
  they may mutate ChezMoi-owned agent, MCP, hook, or provider configuration.

## Sources

- [[_raw/research/cli-tool-discovery--shallow/report]]
