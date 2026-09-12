---
title: Wiki index
type: moc
tags: [wiki]
state: accepted
---

# Wiki index

## Active pages

<!-- The agent maintains links to accepted pages here. Do not list archived pages. -->

- [[target-network-and-operations-topology]] — target network, control-plane,
  and cloud-boundary architecture.
- [[logging-and-observability-architecture]] — central logging, metrics, and
  alerting design.
- [[external-deployment-strategy]] — external GitHub Actions and Tailscale
  deployment control.
- [[herdr-coding-agent-runtime]] — persistent coding-agent runtime, its
  operational boundaries, and official reference links.
- [[cli-tool-discovery-watchlist]] — vetted starting points for finding CLI,
  TUI, and coding-agent tools.

## Open questions and contradictions

<!-- The agent records unresolved questions or conflicting claims here. -->

- Verify the documented home topology against live router, routes, Tailscale
  ACLs, and recovery access before applying it as a migration baseline.
- Decide cloud provider, data residency, alert-routing channel, log retention,
  and the scope of Mail Ops and financial data in cloud logging and backups.
