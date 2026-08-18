---
title: "Home network topology before infrastructure migration"
type: raw-conversation
tags: [conversation, infrastructure, network, tailscale, reliability]
origin: "Codex conversation"
created: 2026-08-18
---

# Home network topology before infrastructure migration

## Initial question

Christian asked whether a clean network topology should be established before
repairing Tailscale, setting up an external GitHub Actions deployment path, or
migrating services to a European cloud provider.

## Consensus / current state

The network foundation is the first prerequisite. The current documented home
design uses OpenWrt `hermes-gateway` as the router and only subnet router for
the LAN (`192.168.8.0/24`) and service VLAN (`192.168.40.0/24`), with Atlas at
`192.168.8.100`. Tailscale should provide the tested management path from
remote clients through the router to these private networks.

The cloud target should not copy the home VLAN layout. It should be a direct,
separately tagged Tailscale node with narrowly scoped ACL access. This keeps
the migration topology simpler than extending home broadcast networks into the
cloud.

## Decisions

1. Create and validate an actual-versus-target network topology before making
   major infrastructure changes.
2. Stabilize the management path (client -> Tailscale -> router -> Atlas),
   including a reboot-resilience test, before CI or cloud migration work.
3. Avoid concurrent changes to DNS, AdGuard, VLANs, and Tailscale; preserve a
   working management and recovery route throughout.
4. Continue with a least-privilege `tag:ci` GitHub Actions path only after the
   topology and Atlas reachability are understood.

## Open questions

- What does the live topology currently look like, including physical uplink,
  switch links, Wi-Fi clients, IP allocation, routes, DNS, and tailnet ACLs?
- Is Atlas intended to be reached only through the router's subnet route, or
  also as a direct Tailscale node?
- Which management/recovery access remains available if OpenWrt or DNS fails?

## Related Wiki pages

- [[atlas-tailscale-and-external-deploy-control]]
- [[european-cloud-migration-atlas--shallow/report]]
