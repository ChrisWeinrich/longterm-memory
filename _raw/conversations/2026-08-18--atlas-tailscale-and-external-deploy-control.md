---
title: "Atlas Tailscale recovery and external deploy control"
type: raw-conversation
tags: [conversation, infrastructure, tailscale, github-actions, reliability]
origin: "Codex conversation"
created: 2026-08-18
---

# Atlas Tailscale recovery and external deploy control

## Initial question

Christian wants to restructure an unstable home infrastructure, potentially
move always-on workloads to a European cloud provider, and understand how to
manage Docker Compose deployments there.

## Consensus / current state

Atlas is currently a single host for workloads and its self-hosted GitHub
Actions runner. The documented July 2026 host hangs showed that this couples a
service-host failure to deployment-control failure. A future cloud deployment
should retain a simple Docker Compose model, with GitHub-hosted Actions
connecting privately through Tailscale as a short-lived, least-privileged CI
node instead of using a runner on the service host.

## Decisions

1. First restore and validate Tailscale reachability to Atlas.
2. Then implement a GitHub Actions deployment connection through Tailscale,
   scoped to a dedicated CI tag and minimal ACL access.
3. Defer cloud-host migration and Proxmox design until this secure control path
   is understood and working.

## Open questions

- What specifically is broken in Atlas Tailscale: Atlas node connection,
  router subnet routes, ACL policy, DNS, or the client route-acceptance state?
- Which exact CI permissions and destination ports are needed for a future
  deployment-only `tag:ci` policy?
- Does the desired cloud target require EU residency generally or Germany
  specifically?

## Related Wiki pages

- [[european-cloud-migration-atlas--shallow/report]]
- [[proxmox-homelab-architecture--shallow/report]]
