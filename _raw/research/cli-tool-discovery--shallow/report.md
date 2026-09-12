---
title: "CLI Tool Discovery Sources — Shallow Research Report"
type: raw-research-report
tags: [research, cli, terminal, tool-discovery, coding-agents]
origin: research-workflow
created: 2026-09-12
---

# CLI Tool Discovery Sources

## Conclusion

Use a small, complementary watchlist instead of one undifferentiated tool
directory. Terminal Trove is useful for broad, category-led discovery; Awesome
Modern CLI is a focused replacement map for traditional Unix commands; Awesome
CLI Apps is an evergreen catalogue; and Awesome CLI Coding Agents is the
agent-runtime and orchestration discovery source. GitHub Topics provide an
early-warning feed but are not curated recommendations.

## Evidence

| Source | Best use | Scope / limitation |
| --- | --- | --- |
| [Terminal Trove categories](https://terminaltrove.com/categories/) | Discover CLI and TUI tools by practical domain | A directory; evaluate individual projects independently |
| [Awesome Modern CLI](https://github.com/thegdsks/awesome-modern-cli) | Find modern replacements for classic terminal tools | Focused on command replacements and terminal workflows |
| [Awesome CLI Apps](https://github.com/agarrharr/awesome-cli-apps) | Search a broad, long-lived command-line catalogue | Broadness makes it less selective |
| [Awesome CLI Coding Agents](https://github.com/bradAGI/awesome-cli-coding-agents) | Discover coding agents, runners, orchestration, and infrastructure | Fast-moving agent ecosystem; verify official upstream docs |
| [GitHub CLI topic](https://github.com/topics/cli) | Spot general projects early | Popularity/topic labels are not review or maintenance proof |
| [GitHub terminal topic](https://github.com/topics/terminal) | Spot terminal-native projects early | Same discovery-only limitation |
| [GitHub cli-agent topic](https://github.com/topics/cli-agent) | Spot emerging CLI-agent projects | Community-assigned topic; includes experimental and unrelated projects |

The current source pages support the intended split: Terminal Trove exposes
categories such as CLI, diff, Git, macOS, network, testing, and TUI; Awesome
Modern CLI groups replacements across file search, text processing, version
control, diff, monitoring, networking, and more; and Awesome CLI Coding Agents
explicitly covers terminal agents plus session managers, parallel runners,
orchestration, and agent infrastructure.

## Candidate tools already identified

- **Herdr** is already covered by [[herdr-coding-agent-runtime]] as an accepted
  runtime evaluation.
- **Hunk** was not previously covered. It is a review-first terminal diff
  viewer for agent-authored changesets. Its official repository documents
  `hunk diff` for reviewing the current working tree and a Homebrew package.
  [Hunk](https://github.com/modem-dev/hunk)

## Trade-offs and risks

- Lists establish discovery value, not suitability, maintenance quality, or
  safety. Check an individual tool's official repository, release cadence,
  license, configuration effects, and permissions before installation.
- Tools that alter agent configuration, MCP registrations, provider routing,
  hooks, or remote access require a ChezMoi-managed design review. Prefer
  read-only review and discovery tools for first trials.
- GitHub topic pages are useful for recency but intentionally include
  experimental projects and loosely applied labels.

## Open questions

- Which discovery sources deserve a recurring review cadence versus occasional
  lookup only?
- Should Hunk receive a dedicated compatibility evaluation after a local trial?

## Sources

All sources were searched and retrieved on 2026-09-12.

- [Terminal Trove categories](https://terminaltrove.com/categories/)
- [Awesome Modern CLI](https://github.com/thegdsks/awesome-modern-cli)
- [Awesome CLI Apps](https://github.com/agarrharr/awesome-cli-apps)
- [Awesome CLI Coding Agents](https://github.com/bradAGI/awesome-cli-coding-agents)
- [GitHub CLI topic](https://github.com/topics/cli)
- [GitHub terminal topic](https://github.com/topics/terminal)
- [GitHub cli-agent topic](https://github.com/topics/cli-agent)
- [Hunk](https://github.com/modem-dev/hunk)
