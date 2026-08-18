---
title: "European cloud migration for Atlas: shallow research"
type: raw-research-report
tags: [research, infrastructure, cloud, scaleway, reliability]
origin: research-workflow
created: 2026-08-18
---

# European cloud migration for Atlas: shallow research

## Conclusion

Moving the Atlas workloads to a European cloud provider is likely a better
first reliability investment than introducing a local Proxmox cluster. It
removes the current local host, power, and physical-network dependency from
always-on services while preserving the existing Debian/Docker Compose model.

Scaleway is the leading candidate because the accepted infrastructure ADR
already chose its S3-compatible Object Storage for off-site backups and
anticipated future compute there. A first cloud deployment should be one
well-sized VM plus block storage and encrypted backups to a separate
Multi-AZ object-storage bucket. This is deliberately not an HA claim: a
single VM remains an application failure domain.

## Evidence

- Scaleway Instances provide provisioned virtual compute, selectable
  availability zones, volumes, public IPs, SSH access, and cloud-init for
  first-boot automation. [Instances quickstart](https://www.scaleway.com/en/docs/instances/quickstart/)
- Scaleway Object Storage is S3-compatible. Its Standard Multi-AZ class stores
  data across three availability zones in Paris, Amsterdam, or Warsaw; Standard
  One Zone is documented as appropriate for secondary backups and recreatable
  data. [Object Storage FAQ](https://www.scaleway.com/en/docs/object-storage/faq/)
- Scaleway operates physical and virtual infrastructure, but its shared
  responsibility documentation assigns customers responsibility for service
  continuity configuration and backup integrity/restore verification.
  [Shared responsibility model](https://www.scaleway.com/en/docs/object-storage/reference-content/storage-shared-responsibility-model/)
- The existing accepted ADR selects Scaleway Object Storage, client-side
  encryption, and later OpenTofu for the home infrastructure; it explicitly
  notes that automated backup and restore drills are not yet implemented.

## Trade-offs and risks

- Cloud compute avoids Atlas hardware failures but makes internet connectivity,
  provider-account recovery, firewalling, patching, and cost monitoring more
  consequential.
- Keep the existing OpenWrt router for home-network duties; do not attempt to
  lift-and-shift its LAN/VLAN/DNS role into the first cloud migration.
- Jellyfin media on USB disks is a poor first cloud-migration candidate due to
  storage, upload, and streaming-egress costs. Migrate its metadata or leave
  it local initially.
- Mail Ops holds personal email data. It needs an explicit data-location,
  retention, encrypted-backup, and public-exposure decision before migration.
- The cloud VM and its backup bucket must not be the only copies of critical
  data. A provider outage, accidental deletion, or account lockout still needs
  a tested alternate restore route.

## Open questions

- Which services must be public or reachable remotely, and which can remain
  private over Tailscale only?
- What are the current CPU, RAM, disk, database, mail, and media sizes, plus
  expected monthly traffic and acceptable monthly budget?
- Is data residency in Germany specifically required, or is EU location enough?
- Should Mail Ops and financial-import data stay at home until a separate
  privacy review, or move under an explicitly accepted EU-cloud policy?

## Sources

- https://www.scaleway.com/en/docs/instances/quickstart/ (retrieved 2026-08-18)
- https://www.scaleway.com/en/docs/object-storage/faq/ (retrieved 2026-08-18)
- https://www.scaleway.com/en/docs/object-storage/reference-content/storage-shared-responsibility-model/ (retrieved 2026-08-18)
- /Users/christianweinrich/Source/infrastructure/docs/decisions/atlas-backup-scaleway-object-storage.md (inspected 2026-08-18)
