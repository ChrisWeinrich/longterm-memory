---
title: "Logging and observability architecture"
type: wiki-page
tags: [infrastructure, observability, logging, monitoring, alerting]
state: draft
created: 2026-08-18
sources:
  - "_raw/research/central-logging-stack--shallow/report.md"
  - "_raw/conversations/2026-08-18--home-network-topology-first.md"
---

# Logging and observability architecture

## Summary

This draft defines a small, central observability design for the home and
future cloud infrastructure. It adds central logs and alerts to the existing
Prometheus/Grafana metrics baseline while avoiding a complex distributed
logging platform.

## Key points

- Run Grafana Alloy on each managed Linux host. It collects Docker
  stdout/stderr and the systemd journal.
- Run Grafana Loki, Grafana, Prometheus, and Alertmanager on an independent
  observability host. Do not run the central log store only on the workload
  host it is intended to diagnose.
- Begin Loki in monolithic/single-binary mode. Do not introduce Kubernetes,
  Loki microservices, or the deprecated simple-scalable deployment mode
  without a measured scale requirement.
- Store Loki's durable data and infrastructure backups in encrypted,
  S3-compatible object storage. Object storage does not remove the need for
  restore verification.
- Reach administrative and observability interfaces through Tailscale only.
  Public exposure is an explicit later design decision.
- Start with 30 days of log retention, then revise the value from actual
  volume, cost, privacy, and operational needs.
- Define alerts first for host-down, container-unhealthy, disk-full,
  backup-failed, and broken Tailscale management paths.

## Data and label policy

- Applications should emit structured logs to stdout/stderr.
- Never log credentials, tokens, authorization headers, e-mail bodies, or
  financial content.
- Use stable, low-cardinality labels only: `environment`, `host`, `service`,
  and `level`.
- Keep request IDs, user IDs, paths, and other high-cardinality values in the
  log payload or structured metadata instead of labels.
- Decide whether Mail Ops and financial-import logs may leave the home network
  before enabling their collection.

## Links

- [[target-network-and-operations-topology]]
- [[_raw/research/central-logging-stack--shallow/report]]
- [[_raw/conversations/2026-08-18--home-network-topology-first]]

## Open questions and contradictions

- Select the Alertmanager notification channel and escalation policy.
- Confirm the retention period, S3 cost budget, and data-residency requirement.
- Confirm whether an independent observability host can be created before the
  application cloud migration.
- The current repository's observability stack is metrics-only; the exact
  migration path from its Atlas-local Grafana/Prometheus deployment remains to
  be designed and validated.
