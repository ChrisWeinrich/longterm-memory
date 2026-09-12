---
title: "Filter-Konfigurations-Metadatenmodell als erster Baustein"
type: raw-conversation
tags: [conversation, dotnet, api, entity-framework, filters, metadata]
origin: codex-conversation
created: 2026-08-26
---

# Filter-Konfigurations-Metadatenmodell als erster Baustein

## Initial question

Was ist der erste konkrete Baustein für die metadata-getriebene,
relationale Such- und Anzeige-API?

## Consensus / current state

- Die Filter- und Anzeigefeldkonfiguration ist bereits als Backend-Konzept
  gesetzt.
- Als nächster und erster Baustein wird ein Filter-Konfigurations-
  Metadatenmodell benötigt, bevor Query-Compiler oder Endpoint implementiert
  werden.
- Das Modell soll Felder über relationale Pfade wie `Name`, `City.Name` und
  `City.Street.Name` unterstützen und viele konfigurierbare Filter abbilden.
- Die spätere UI referenziert stabile Feldschlüssel; sie übergibt keine freien
  Datenbankpfade, SQL- oder LINQ-Ausdrücke.

## Decisions

- Das Metadatenmodell für Filter und Anzeige wird vor dem generischen
  EF-Core-Query-Compiler und dem Suchendpoint entworfen.

## Open questions

- Werden Felddefinitionen global pro Root-Entity wiederverwendet und nur je
  View konfiguriert, oder werden sie vollständig pro View gespeichert?
- Wie werden Collection-Navigationen und deren `Any`-/`All`-Semantik im
  Pfadmodell dargestellt?
- Welche Operatoren, Datentypen, Berechtigungen, Sortierbarkeit und
  Projektionseigenschaften müssen in Version 1 unterstützt werden?
- Bleibt der relationale Pfad ein internes, versionsabhängiges Mapping oder
  soll er vollständig administrierbar sein?

## Related Wiki pages

- [[_raw/conversations/2026-08-26--metadata-driven-relational-query-builder]]
- [[_raw/research/dotnet-transitive-query-api--shallow/report]]

