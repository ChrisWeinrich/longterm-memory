---
title: "ChezMoi AI structure review"
type: raw-conversation
tags: [conversation, chezmoi, ai-configuration, architecture]
origin: "Codex conversation"
created: 2026-08-18
---

# ChezMoi AI structure review

## Initial question

Christian asked for a deeper assessment of the ChezMoi repository because the
mix of general configuration, AI configuration, MCPs, skills, launchers, and
automation is difficult to understand.

## Consensus / current state

The repository has a coherent technical model: ChezMoi is the source of truth;
shared templates define common MCPs, instructions, and permissions; agent
directories adapt those values for Codex, Claude, and Copilot; merge templates
preserve application-owned runtime state; and apply hooks synchronize skills,
install curated skills, configure integrations, and remove legacy duplicates.

The main usability issue is conceptual discoverability. The AI stack spans
`.chezmoitemplates/`, `dot_codex/`, `dot_claude/`, `dot_copilot/`,
`dot_agents/`, `dot_local/bin/`, `dot_config/`, `dot_claude-mem/`,
`Library/LaunchAgents/`, and `run_after_*` hooks. This source layout follows
ChezMoi deployment targets rather than a single domain-oriented AI entry point.

The review also observed duplicated retired-MCP cleanup lists across the three
agent adapters, with Codex additionally removing `memory`, and a documentation
inconsistency: `AGENTS.md` says the Claude-skill sync hook applies on private
and business, while the hook exits immediately on business.

## Open questions

- Should the repository add a concise AI architecture map describing ownership,
  source-to-target paths, and the `chezmoi apply` lifecycle?
- Should retired MCP definitions be centralized, or should the intentional
  differences between agent adapters be documented explicitly?
- Should the business behavior of the Claude skill-sync hook and its
  documentation be aligned?

## Related Wiki pages

No related accepted Wiki page was found during capture.
