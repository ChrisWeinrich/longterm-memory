---
title: "Infrastructure Current-State Assessment"
type: research-report
tags: [assessment, infrastructure, operations, repository]
state: accepted
created: 2026-08-12
source_repository: "/Users/christianweinrich/Source/infrastructure"
source_revision: "23847ca"
research_scope: repository-only
---

# Infrastructure Current-State Assessment

## Conclusion

This is a repository-state assessment, not a live-health assessment. At commit
`23847ca` (2026-08-11), the repository defines one primary home site with one
router (**hermes-gateway**) and one application host (**atlas-host**). Atlas is
the central failure domain: it is the Docker Compose host for the documented
services and also runs the self-hosted GitHub Actions runner that validates and
deploys those services.

The codebase contains substantial declarative automation and operational
documentation: Ansible configures the host and router; Compose definitions
describe the application stacks; GitHub Actions performs validation and deploys
from `main`; and a Prometheus/Grafana metrics stack exists. However, the
repository explicitly documents that centralized logs and alerting are not yet
in scope, the server-side backup application is a placeholder, and the
repository cannot establish that its documented configurations are currently
applied or healthy.

## Assessment method and evidence boundary

The sole source was `/Users/christianweinrich/Source/infrastructure`. I read
the tracked root guidance, inventories, network configuration, Ansible
playbooks and roles, application definitions, Compose templates, workflows,
runbooks, tracked snapshots, and recent Git history. No host, router, service,
GitHub API, log, metric, or backup command was run.

Labels used below:

- **Implemented configuration** — tracked automation/configuration defines the
  behavior.
- **Documented procedure** — a tracked document describes intended operations.
- **Repository inference** — conclusion from multiple tracked artifacts.
- **Unknown from repository evidence** — requires live verification.

## Topology and control paths

| Area | Current repository evidence | Classification |
| --- | --- | --- |
| Home network | `192.168.8.0/24` LAN, routed by `hermes-gateway` at `192.168.8.1`; Atlas is `192.168.8.100`. | Implemented configuration — `ansible/inventories/home/hosts.yml`, `ansible/configs/network.yml` |
| Service network | VLAN 40 (`192.168.40.0/24`) is trunked to Atlas; Docker services use the external `vlan40_macvlan` network and fixed service addresses. | Implemented configuration — `ansible/configs/network.yml`, `ansible/playbooks/server.yml`, `ansible/roles/server/docker/macvlan/` |
| Remote access | The router advertises LAN and VLAN 40 through Tailscale. Tailnet approval, client route acceptance, and ACLs still require separate verification/manual action. | Implemented configuration plus documented procedure — `ansible/inventories/home/group_vars/routers.yml`, `docs/runbooks/openwrt-verification.md` |
| Router DNS filtering | The desired AdGuard/dnsmasq split exists, but `router_adguard_enabled: false` is the current tracked safe default after an April 2026 DNS rollback incident. The active WWAN station configuration is documented as live-only, not repository-templated. | Implemented configuration and documented limitation — `ansible/inventories/home/group_vars/routers.yml`, `docs/runbooks/network-config.md` |
| Host control plane | `server.yml` configures hostname, VLAN, USB drives, Docker, Compose, macvlan, operator debugging, a hardware/kernel watchdog, and object-store tenants. | Implemented configuration — `ansible/playbooks/server.yml` |
| Application deployment | `compose-deploy.yml` validates every push/PR and deploys `main` only after validation, on `[self-hosted, linux, x64]`. `compose-deploy.sh` discovers non-skipped apps, runs hooks, renders templates, then runs `docker compose up -d`. | Implemented configuration — `.github/workflows/compose-deploy.yml`, `scripts/compose-deploy.sh` |

**Repository inference:** Atlas is a combined workload, CI validation, and
deployment host. A host outage therefore removes the services and the normal
path to validate/deploy them at the same time. This is explicitly consistent
with the reliability incident record, which says the runner was unavailable
while Atlas was down.

## Defined workload inventory

`apps/infra/` and `apps/user/` contain nine non-skipped application
definitions. `apps/bootstrap/github-runner/` is a separate bootstrap-only
stack and is manually deployed by design. `apps/infra/backup/` is discoverable
but skipped and has no Compose stack.

| Workload | Role and persistent state | Classification |
| --- | --- | --- |
| PostgreSQL / pgvector | Primary database on VLAN 40; data bind-mounted below `/srv/containers/volumes/postgres/`; a Compose health check and post-deploy app-role bootstrap are defined. | Implemented configuration — `apps/infra/postgres/`, `ansible/vars/constants.yml` |
| MinIO | S3-compatible object store on VLAN 40; its MinIO data directory is durable and tenant provisioning is included in `server.yml`. | Implemented configuration — `apps/infra/object-store/`, `ansible/roles/apps/object_store_tenants/` |
| Teable | VLAN 40 workspace app depending on PostgreSQL, Redis, and MinIO; Redis append-only data and Teable data are persisted. | Implemented configuration — `apps/infra/teable/` |
| Observability | Prometheus, Grafana, node_exporter, and cAdvisor; Prometheus and Grafana data/config are persisted. | Implemented configuration — `apps/infra/observability/` |
| Mail operations | Local IMAP mirror, Notmuch, findings, state, and logs; a sync-age health check is defined. | Implemented configuration — `apps/infra/mail-ops/` |
| Bank operations | Local image worker that imports bank statements into PostgreSQL and mounts data/log paths. | Implemented configuration — `apps/infra/bank-ops/` |
| Jellyfin | User-facing media service on VLAN 40 with persistent configuration under the durable-volume root. | Implemented configuration — `apps/user/jellyfin/` |
| Sample workloads | `hello-world-nginx` and `postgres-mvp-app` remain non-skipped test/MVP definitions. | Implemented configuration — `apps/user/hello-world-nginx/`, `apps/user/postgres-mvp-app/` |
| GitHub Actions runner | Persistent org-level runner on Atlas, with Docker socket access and `restart: always`; it is intentionally outside normal Compose discovery. | Implemented configuration and documented procedure — `apps/bootstrap/github-runner/`, `docs/runbooks/github-runner-mvp.md` |

`skip: false` defines deployment eligibility, not proof that a workload is
currently running. Actual containers, image versions, health-check state,
network attachment, and durable data contents are **unknown from repository
evidence**.

## Delivery, configuration, and change evidence

- **Implemented configuration:** CI linting and Compose validation both run on
  the same self-hosted runner. Deployment is restricted to `main`; normal
  manual `--run` is rejected by the script. The runner itself is the documented
  manual bootstrap exception. Paths: `.github/workflows/ci.yml`,
  `.github/workflows/compose-deploy.yml`, `scripts/compose-deploy.sh`,
  `docs/runbooks/github-runner-mvp.md`.
- **Implemented configuration:** app pre-hooks validate or render inputs; the
  deploy workflow checks required secrets before invoking the deploy script.
  The script captures per-app outcomes for its run summary, but it invokes
  `docker compose up -d` and contains no general rollback operation. Paths:
  `scripts/compose-deploy.sh`, `.github/workflows/compose-deploy.yml`.
- **Implemented configuration:** Ansible records start/final deployment rows
  and router UCI snapshots under `snapshots/`. The tracked deployment history's
  latest Atlas success is 2026-07-22 at commit `40525cf`, not the current
  repository revision. This is historical evidence only, not proof of current
  drift or failure. Paths: `ansible/roles/shared/deployment-history/`,
  `snapshots/ansible-deployment-history.md`, `snapshots/README.md`.
- **Repository inference:** the recent history shows several fixes to
  observability networking/mounts and two mail-ops health-check rendering fixes
  on 2026-08-10/11. This demonstrates active correction of deployment details;
  it does not establish whether current production state includes those fixes.
  Evidence: `git log` at `23847ca`; relevant paths include
  `apps/infra/observability/` and `apps/infra/mail-ops/`.

## Observability and operational access

- **Implemented configuration:** Prometheus scrapes itself, node_exporter, and
  cAdvisor every 15 seconds. Grafana has provisioned host/container dashboards.
  This provides host and Docker-container metrics, not application-specific
  instrumentation. Paths: `apps/infra/observability/config/prometheus/prometheus.yml.tmpl`,
  `apps/infra/observability/compose/docker-compose.yml.tmpl`.
- **Documented procedure:** Grafana is intended to be reached from the LAN at
  `192.168.40.10:3000`; troubleshooting and manual health checks are recorded
  in the observability runbook. Path: `docs/runbooks/atlas-observability.md`.
- **Documented limitation:** Loki/log aggregation and alerting are explicitly
  out of scope for the current phase. The same runbook identifies no
  Alertmanager and no host-down/hang alert. Path:
  `docs/runbooks/atlas-observability.md`, `docs/runbooks/atlas-reliability.md`.
- **Implemented configuration with security consequence:** the Atlas operator
  account is granted journal/log read groups, writable ACLs on `/opt/compose`,
  and Docker access. The repository labels this temporary high-blast-radius
  convenience; logs and Compose paths may expose secrets. Paths:
  `ansible/roles/server/access/operator-debug/`,
  `docs/runbooks/atlas-operator-debug.md`, `AGENTS.md`.

## Reliability, backup, and recovery evidence

- **Documented incident and implemented mitigation:** Atlas is documented as
  having suffered a kernel-oops hang (2026-07-01) and a userspace/Docker wedge
  (2026-07-16). The default-enabled watchdog role configures kernel panic/oops
  reboots and a systemd hardware watchdog. A destructive recovery drill is
  documented but not evidenced as completed. Paths:
  `docs/runbooks/atlas-reliability.md`,
  `ansible/roles/server/reliability/watchdog/defaults/main.yml`,
  `ansible/roles/server/reliability/watchdog/tasks/main.yml`.
- **Documented procedure:** durable data is expected under
  `/srv/containers/volumes`, with explicit consistency caveats for PostgreSQL,
  MinIO, and Prometheus. The phase-one backup flow is Mac-side rsync followed
  by encrypted local restic; logical PostgreSQL dumps and restore drills are
  recommended. Paths: `ansible/vars/constants.yml`,
  `docs/runbooks/atlas-durable-data.md`,
  `docs/runbooks/atlas-backup-local-mac.md`,
  `scripts/atlas-backup-local-mac.sh`.
- **Documented limitation:** default backup excludes maildir; USB media and the
  router are outside its scope. The server-side backup app is explicitly not
  implemented. The accepted Scaleway ADR selects a future off-site target but
  states that no automated backup job is defined yet. Paths:
  `docs/runbooks/atlas-backup-local-mac.md`, `apps/infra/backup/README.md`,
  `docs/decisions/atlas-backup-scaleway-object-storage.md`.
- **Unknown from repository evidence:** whether backups run on schedule,
  complete successfully, include logical database dumps, meet a recovery target,
  or have passed a real restore drill.

## Known gaps and uncertainty for the next discussion

These are observations, not recommendations:

1. The current observability phase has metrics for Atlas and Docker but no
   centralized log pipeline or alerting. This is explicitly documented, rather
   than inferred.
2. Atlas remains the documented single host for services, runner, and local
   durable data. The repo has watchdog recovery, but no alternate compute host
   or externally independent deployment executor is defined.
3. The backup design is partly operational documentation and workstation
   tooling; the in-repo backup stack and automated off-site implementation are
   not defined as deployed systems.
4. Router management retains a live-only WWAN station detail, and the AdGuard
   feature is intentionally disabled after a rollback. The repo therefore does
   not fully represent all router runtime configuration.
5. Repository evidence cannot answer the immediate operational questions that
   matter most during an incident: which services are up, what failed first,
   whether alerts fire, whether the runner is online, how full disks are, or
   whether restore paths work.

## Evidence paths

- Repository contract and topology: `AGENTS.md`,
  `ansible/inventories/home/hosts.yml`, `ansible/configs/network.yml`
- Host/router automation: `ansible/playbooks/server.yml`,
  `ansible/playbooks/router.yml`, `ansible/roles/server/`, `ansible/roles/router/`
- Workloads and deployment: `apps/`, `scripts/compose-deploy.sh`,
  `.github/workflows/ci.yml`, `.github/workflows/compose-deploy.yml`
- Operations and recovery: `docs/runbooks/atlas-observability.md`,
  `docs/runbooks/atlas-reliability.md`, `docs/runbooks/atlas-backup-local-mac.md`,
  `docs/runbooks/network-config.md`, `snapshots/`

## Sources

This report intentionally uses repository paths rather than external URLs; no
external sources or live systems were queried.
