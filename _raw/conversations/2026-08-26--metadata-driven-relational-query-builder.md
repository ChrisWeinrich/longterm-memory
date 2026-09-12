---
title: "Metadata-getriebener relationaler Query Builder in .NET"
type: raw-conversation
tags: [conversation, dotnet, api, entity-framework, query-builder, filters]
origin: codex-conversation
created: 2026-08-26
---

# Metadata-getriebener relationaler Query Builder in .NET

## Initial question

Wie lässt sich in .NET ein Endpoint gestalten, der eine Hauptentität mit
variablen Filtern und variabler Ausgabe durchsucht, auch über mehrstufige
FK-/Navigationsbeziehungen?

## Consensus / current state

- Die für Filter und Anzeige verfügbaren Felder werden bereits im Backend
  gespeichert und konfiguriert.
- Beispiele für konfigurierte Pfade sind `Name`, `City.Name` und
  `City.Street.Name`; es gibt viele konfigurierbare Filter.
- Die UI soll keine DB-Feldpfade, SQL oder freie LINQ-Ausdrücke senden. Sie
  übermittelt Feldschlüssel, erlaubte Operatoren, Werte und gewünschte Spalten.
- Das Backend löst die Feldschlüssel gegen die gespeicherte
  Feldkonfiguration auf, validiert sie und kompiliert daraus eine EF-Core-
  `IQueryable`-Abfrage beziehungsweise Expression Trees.
- Das ist ein metadata-getriebener LINQ-/EF-Core-Query-Builder, kein Builder
  für zusammengesetzte SQL-Strings. EF Core erzeugt das parametrisierte SQL und
  die notwendigen Joins oder Unterabfragen.
- GraphQL und OData sind mögliche externe Query-Sprachen, werden für dieses
  Backend-gesteuerte Modell aber nicht benötigt, solange der eigene Endpoint
  die konfigurierte Query-DSL kontrolliert.

## Open questions

- Wie sind Felddefinitionen genau modelliert: Feldschlüssel, Root-Entity,
  Pfad, Datentyp, erlaubte Operatoren, Berechtigungen und Ausgabealias?
- Wie werden Collection-Pfade modelliert, insbesondere `Any`/`Some`-Semantik?
- Welches Rückgabeformat benötigt die dynamische Spaltenauswahl: typisierte
  View-DTOs, generische Rows oder JSON-Objekte?
- Welche Limits sind nötig: maximale Navigationstiefe, Seitenlänge,
  Sortierung, Query-Timeout und erlaubte Pfade?
- Wie werden Mandanten- und Zeilenberechtigungen zwingend vor jeder
  konfigurierbaren Filterung angewendet?

## Related Wiki pages

- [[_raw/research/dotnet-transitive-query-api--shallow/report]]

