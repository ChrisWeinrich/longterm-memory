---
title: "Herdr — Research Query"
type: research-query
tags: [research, herdr, coding-agents, terminals, orchestration, plugins]
state: accepted
created: 2026-09-12
---

# Deep research query

Research this question: What can Herdr from `herdr.dev` do as the runtime that
coding agents live in, and how can its official documentation be distilled
into safe, easy-to-access Kustos knowledge for agents?

Use the accepted outline as the scope. Prefer Herdr's own documentation,
agent guide, source repository, release notes, and license. Use reputable
secondary sources only for context that official material does not cover.
Record source URLs, publication dates when available, evidence, uncertainty,
and any inference separately from sourced facts.

Verify in particular: supported agent CLIs and detection; terminal and session
state semantics; restart and resume limitations; local socket API and CLI;
remote-machine and SSH behavior; configuration; plugin and marketplace trust
boundaries; supported operating systems; installation and update paths; and
network, access-control, and secret-handling implications. Treat versioned
features and marketplace listings as time-sensitive and record the retrieval
date.

The completed report must include an "Agent quick reference" with the official
documentation index, agent guide, quick start, concepts, supported agents,
configuration, session state, remote machines, API, and plugins links.

Write the completed report to `_raw/research/herdr-dev/report.md` from
`_templates/raw-research-report.md`. It is Raw material without a state and is
curated into `wiki/pages/` later.
