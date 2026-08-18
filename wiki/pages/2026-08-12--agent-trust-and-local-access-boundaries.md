---
title: "Agent Trust and Local Access Boundaries"
type: discussion
tags: [agents, security, trust-boundaries]
state: accepted
created: 2026-08-12
migrated_from: wiki/sources
conversation:
  system: codex
  session_id: "019fe785-aded-7972-b916-e17cae78ca20"
  location: "/Users/christianweinrich/.codex/sessions/2026/08/09/rollout-2026-08-09T19-15-25-019fe785-aded-7972-b916-e17cae78ca20.jsonl"
  availability: local
---

# Agent Trust and Local Access Boundaries

## Starting question

What does broad local file access mean for coding agents and other CLIs, and
what is the relevant security boundary when they can reason over the files they
can read?

## Current consensus

Normal command-line tools run with the permissions of the current macOS user.
Codex's `workspace-write` mode constrains writes, but it is not a strict
read-only allowlist for a single repository. `AGENTS.md` controls agent
behavior, not operating-system access.

The meaningful risk is not limited to a tool matching a known secret with a
simple pattern. A capable agent can combine filenames, source code, logs,
configuration, documentation, and metadata to infer which material is
sensitive or operationally valuable. Therefore the trust boundary includes the
vendor and model, but also prompts, installed plugins and skills, MCP servers,
dependencies, and any tool capable of transmitting data.

For trusted local development tools, broad access is a normal and deliberate
trade-off. For an untrusted agent or code path that must only see a narrow
knowledge collection, the boundary must be enforced outside the agent's
instructions: for example by a separate macOS user, container, or VM with only
the intended files available.

## Open questions

- Which agent classes are trusted enough to run under Christian's primary
  macOS account, and which must use an isolated environment?
- What minimum collection of files and MCP capabilities does each specialized
  assistant need?
- How should outbound network access and MCP/plugin provenance be reviewed for
  isolated agent environments?

## Related wiki pages

- [[2026-08-12--wiki-as-shared-long-term-memory|Wiki as shared long-term memory]]
