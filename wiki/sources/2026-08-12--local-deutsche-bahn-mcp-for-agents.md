---
title: "Lokales Deutsche-Bahn-MCP für Agenten"
type: discussion
tags: [agents, deutsche-bahn, infrastructure, mcp]
state: accepted
created: 2026-08-12
---

# Lokales Deutsche-Bahn-MCP für Agenten

## Ausgangsfrage

Wie sollen persönliche Agenten zuverlässig auf Deutsche-Bahn- und
Mobilitätsdaten zugreifen?

## Konsens / aktueller Stand

Das untersuchte externe MCP von Paul von Berg soll nicht als gehosteter Dienst
übernommen werden: Sein öffentlicher Endpoint ist stillgelegt, es gibt einen
offenen Session-Fehler und die Wartung ist begrenzt. Der DB API Marketplace
bietet einen kostenlosen Einstieg mit eigenen Zugangsdaten, jedoch unter
API-spezifischen Lizenz- und Nutzungsbedingungen.

## Entscheidungen

- Das Thema wird als Infrastrukturarbeit weiterverfolgt.
- Es soll ein eigener, schlanker und lokal ausgeführter MCP für Agenten
  entstehen.
- Der MCP soll bevorzugt direkt die offiziellen DB-APIs nutzen und zunächst
  ausschließlich lesende Funktionen anbieten.
- Der Startumfang soll klein bleiben: Stationssuche, Abfahrten/Fahrpläne und
  Störungen; Parken und Barrierefreiheit folgen nur bei tatsächlichem Bedarf.
- Zugangsdaten gehören in den bestehenden Secret-Workflow, nicht in
  Repository-Dateien oder MCP-Client-Konfigurationen.

## Offene Punkte

- Konkreter Repository-Pfad und Laufzeitmodell (lokales stdio-only vs.
  Netzwerktransport).
- Gewünschte erste Tool-Schnittstellen und Antwortformate.
- Prüfung der aktuellen DB-API-Lizenzen, Limits und Attributionspflichten vor
  Implementierung weiterer Datenquellen.
- Versionierung und Tests gegen die verwendeten MCP-Clients.

## Verwandte Wiki-Seiten

- [[2026-08-12--paulvonberg-db-mcp-server--shallow|Shallow Research zum bestehenden DB-MCP]]
- [[2026-08-12--infrastructure-current-state|Infrastructure Current-State Assessment]]
