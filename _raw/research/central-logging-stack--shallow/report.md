---
title: "Central logging stack for the home and cloud infrastructure: shallow research"
type: raw-research-report
tags: [research, infrastructure, observability, logging, loki, grafana]
origin: research-workflow
created: 2026-08-18
---

# Central logging stack for the home and cloud infrastructure: shallow research

## Conclusion

Use a deliberately small Grafana-based stack: Grafana Alloy on every managed
Linux host to collect journald and Docker container stdout/stderr; one central
Grafana Loki instance to retain and query logs; Grafana for exploration; and
Prometheus plus Alertmanager for availability and log-derived alerts. Run the
central stack on a separate small cloud VM, not inside the Atlas or future
application stack, and use Scaleway S3-compatible Object Storage for Loki's
durable data.

For the anticipated volume, use Loki monolithic/single-binary mode, not
Kubernetes, microservices mode, OpenSearch, or ELK. Start with a 30-day
retention policy and adjust from observed volume and operational value. Add
traces only when a specific application debugging need justifies them.

## Evidence

- Grafana documents monolithic Loki as the simplest deployment mode and
  suitable for small read/write volumes (approximately up to 20 GB/day).
  [Loki deployment modes](https://grafana.com/docs/loki/latest/get-started/deployment-modes/)
- Grafana recommends microservices mode only for very large clusters or when
  operators need precise scale/cluster control; the intermediate simple
  scalable mode is deprecated for Loki 4.0. [Loki deployment
  modes](https://grafana.com/docs/loki/latest/get-started/deployment-modes/)
- Promtail has been deprecated and removed in current Loki releases; its
  functionality moved to Grafana Alloy. [Loki release notes](https://grafana.com/docs/loki/latest/release-notes/v3-4/)
- The official quickstart uses Docker Compose and pairs Loki, Alloy, and
  Grafana for collection and query. [Loki quickstart](https://grafana.com/docs/loki/latest/get-started/quick-start/quick-start/)
- The existing Atlas observability runbook already uses Prometheus, Grafana,
  node_exporter, and cAdvisor, while documenting logs and alerting as
  out-of-scope gaps.

## Trade-offs and risks

- Central logs can contain sensitive values. Applications must write structured
  logs to stdout without credentials, authorization headers, full mail bodies,
  or financial records; collector-side redaction is a safety net, not a primary
  control.
- Loki labels must remain low-cardinality. Stable labels such as environment,
  host, service, and severity are appropriate; request IDs, user IDs, paths,
  and timestamps belong in the log payload or structured metadata.
- If Loki runs on the application host, a host outage also removes the best
  evidence for diagnosing it. A separate observability VM reduces that failure
  coupling but does not replace backups or alerting.
- Object storage preserves data but does not make the Loki query instance
  highly available. Begin with restore/redeploy capability rather than an
  unnecessary Loki cluster.

## Open questions

- Which notification channel should Alertmanager use for critical alarms?
- What data must never leave the home network, especially for Mail Ops and
  financial-import services?
- How long must logs be retained, and what monthly storage budget is
  acceptable?
- Which services are critical enough to require an immediate host-down,
  container-unhealthy, disk-full, backup-failed, and Tailscale-path alert?

## Sources

- https://grafana.com/docs/loki/latest/get-started/deployment-modes/ (retrieved 2026-08-18)
- https://grafana.com/docs/loki/latest/release-notes/v3-4/ (retrieved 2026-08-18)
- https://grafana.com/docs/loki/latest/get-started/quick-start/quick-start/ (retrieved 2026-08-18)
- /Users/christianweinrich/Source/infrastructure/docs/runbooks/atlas-observability.md (inspected 2026-08-18)
