---
title: "Topology before workload inventory"
type: raw-conversation
tags: [conversation, infrastructure, network, containers, migration]
origin: "Codex conversation"
created: 2026-08-18
---

# Topology before workload inventory

## Initial question

Christian clarified the desired order for the infrastructure redesign and
noted that PostgreSQL is not currently relevant.

## Consensus / current state

The current container set is not the future architecture by default. It must
be reviewed after the network topology and management/recovery paths have been
validated. PostgreSQL is currently not a relevant workload.

## Decisions

1. Validate and document the network topology first.
2. Then inventory every current container and classify it as keep, migrate,
   archive, or retire before designing cloud capacity or migration steps.
3. Do not treat PostgreSQL as an assumed required service in the target design.
4. Preserve or back up durable data before retiring a container or volume.

## Open questions

- Which containers and volumes are currently running, and which contain unique
  data?
- Which services have an active user or operational purpose today?
- Which local-only workloads, such as media services, should remain outside a
  first cloud migration?

## Related Wiki pages

- [[target-network-and-operations-topology]]
- [[external-deployment-strategy]]
