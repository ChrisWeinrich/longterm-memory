---
title: "Persönliches Finanz- und Marktdaten-Dashboard – Rechercheauftrag"
type: research-query
tags: [research, finance, market-data, dashboard]
state: accepted
created: 2026-08-21
---

# Deep research query

Research this question: Wie kann Christian ein persönliches Finanz- und
Marktdaten-Dashboard aufbauen oder auswählen, das seine eigenen Bestände und
wichtige Märkte (Aktien/ETFs, Indizes, Anleihen bzw. Renditen, Zinsen, FX und
optional Krypto) nachvollziehbar, datensparsam und langfristig wartbar zeigt?

Use the accepted outline as the scope. Prefer original and official sources,
then peer-reviewed research, then reputable secondary analysis for context.
For every candidate product and API, verify documented features, supported
import/synchronisation paths, licence/terms, pricing, market coverage and data
latency. Prefer sources from the project maintainers, data providers, exchanges,
central banks and regulators. Record source URLs, publication dates when
available, evidence, uncertainty, and any inference separately from sourced
facts.

Compare build-versus-buy options in three practical tiers:

1. Existing product with manual import or a privacy-preserving connection.
2. Self-hosted portfolio tracker plus a separate market-monitoring view.
3. A custom dashboard with a local database and documented market-data APIs.

For the custom tier, define a narrow MVP: canonical instrument identifiers;
transactions and cash; daily portfolio valuation; a market-watchlist; charts
for allocation, performance, index levels and sovereign yields; scheduled data
updates; backups; and secrets handling. Discuss when EOD or delayed data is
appropriate and when real-time data entails cost or licensing constraints.

Write the completed report to
`_raw/research/personal-finance-market-dashboard/report.md` from
`_templates/raw-research-report.md`. It is Raw material without a state and is
curated into `wiki/pages/` later.
