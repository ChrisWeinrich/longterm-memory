---
title: "Proxmox for a resilient home infrastructure: shallow research"
type: raw-research-report
tags: [research, infrastructure, homelab, proxmox, backup]
origin: research-workflow
created: 2026-08-18
---

# Proxmox for a resilient home infrastructure: shallow research

## Conclusion

Proxmox VE is a plausible next host platform for a home infrastructure, but it
does not make a one-node installation highly available. Its immediate value is
workload isolation, reproducible guest restores, and a clean boundary between
the hypervisor and application operating systems. Availability across a host
failure needs independently powered compute nodes, quorum-aware clustering,
and storage/backup design; it should not be the first migration objective.

Proxmox Backup Server (PBS) is valuable even without a cluster when it runs on
separate storage or hardware. It provides incremental, deduplicated,
client-side-encryptable backups, integrity verification, and supports both PVE
guests and physical-host file backups.

## Evidence

- Proxmox VE integrates KVM and LXC and supports local, shared, and
  distributed storage. Its official hardware guidance calls for CPU
  virtualization support, fast redundant storage, and additional memory for
  ZFS or Ceph; it explicitly distinguishes evaluation minimums from production
  hardware. [PVE hardware requirements](https://proxmox.com/en/products/proxmox-virtual-environment/requirements)
- Proxmox states that clustering centrally manages multiple PVE installations.
  This supports the inference that a single PVE node remains a single physical
  failure domain even though it can isolate workloads. [PVE hardware
  requirements](https://proxmox.com/en/products/proxmox-virtual-environment/requirements)
- PBS supports VM, container, and physical-host backups; its official
  documentation describes deduplication, incremental transfers, SHA-256
  integrity checking, remote sync, and client-side encryption. [PBS
  introduction](https://pbs.proxmox.com/docs/introduction.html)

## Trade-offs and risks

- Running PVE, PBS, and all application data on the same physical Atlas host
  improves recovery convenience but does not protect against Atlas, power, or
  local-disk failure.
- A cluster adds operational surface (quorum, networking, storage and upgrade
  coordination). Ceph is particularly unsuitable as an early step unless
  there are sufficient nodes, disks, RAM, and networking to justify it.
- VM-level backups do not replace application-consistent backups. PostgreSQL
  needs logical dumps or database-aware recovery verification; object stores
  and mail data need explicit scope and restore tests.

## Open questions

- Which failures have actually occurred beyond the two July Atlas hangs:
  power, storage, network/router, configuration changes, or application
  failures?
- What hardware, disks, RAM, NICs, UPS, and spare device are available or
  acceptable to buy?
- What recovery objectives apply to each service: may Jellyfin be offline for
  days while mail, databases, and network services require faster recovery?
- Is the intended target a simpler, robust single-node platform with verified
  off-site restore, or host-failure availability through two or more nodes?

## Sources

- https://proxmox.com/en/products/proxmox-virtual-environment/requirements (retrieved 2026-08-18)
- https://pbs.proxmox.com/docs/introduction.html (retrieved 2026-08-18)
