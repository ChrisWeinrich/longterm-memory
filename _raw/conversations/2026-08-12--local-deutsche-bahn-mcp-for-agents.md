---
title: "Lokales Deutsche-Bahn-MCP für Agenten"
type: raw-conversation
tags: [agents, deutsche-bahn, infrastructure, mcp]
origin: legacy-wiki-draft
created: 2026-08-12
legacy_path: wiki/sources/2026-08-12--local-deutsche-bahn-mcp-for-agents.md
---

# Lokales Deutsche-Bahn-MCP für Agenten

## Initial question

Wie sollen persönliche Agenten zuverlässig auf Deutsche-Bahn- und
Mobilitätsdaten zugreifen?

## Consensus / current state

Das untersuchte externe MCP von Paul von Berg wird nicht als gehosteter Dienst
übernommen: Sein öffentlicher Endpoint ist stillgelegt, es gibt einen offenen
Session-Fehler und die Wartung ist begrenzt. Der DB API Marketplace bietet
einen kostenlosen Einstieg mit eigenen Zugangsdaten, jedoch unter
API-spezifischen Lizenz- und Nutzungsbedingungen.

## Decisions

- Das Thema wird als Infrastrukturarbeit weiterverfolgt.
- Es entsteht ein eigener, schlanker und lokal ausgeführter MCP für Agenten.
- Der MCP nutzt bevorzugt offizielle DB-APIs und bietet zunächst nur lesende
  Funktionen.
- Der Startumfang bleibt klein: Stationssuche, Abfahrten/Fahrpläne und
  Störungen; Parken und Barrierefreiheit folgen nur bei Bedarf.
- Zugangsdaten gehören in den Secret-Workflow, nicht in Repository-Dateien
  oder MCP-Client-Konfigurationen.

## Open questions

- Repository-Pfad und Laufzeitmodell (lokales stdio-only oder Netzwerktransport).
- Erste Tool-Schnittstellen und Antwortformate.
- Aktuelle DB-API-Lizenzen, Limits und Attributionspflichten.
