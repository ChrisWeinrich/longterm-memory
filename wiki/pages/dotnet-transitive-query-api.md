---
title: ".NET: variable Query-API über Entitätsbeziehungen"
type: research-report
tags: [research, dotnet, api, graphql, odata, entity-framework]
state: draft
created: 2026-08-26
sources:
  - "_raw/research/dotnet-transitive-query-api--shallow/report.md"
  - "_raw/conversations/2026-08-26--filter-metadata-model-first.md"
  - "_raw/conversations/2026-08-26--metadata-driven-relational-query-builder.md"
---

# .NET: variable Query-API über Entitätsbeziehungen

## Conclusion

Für das beschriebene Backend ist der nächste Baustein ein Metadatenmodell für
Filter- und Anzeigefelder. Es löst stabile UI-Feldschlüssel gegen erlaubte
relationale Pfade, Operatoren und Projektionen auf; erst danach kompiliert ein
kontrollierter EF-Core-Query-Builder die Abfrage.

GraphQL mit Hot Chocolate und OData 8 bleiben Alternativen, falls das Produkt
eine allgemeine externe Query-Sprache benötigt. Die bestätigte Projektentscheidung
ist jedoch, zuerst die eigene, fachlich begrenzte Metadaten- und Query-Schicht
zu entwerfen.

## Evidence

| Wahl | Wann |
| --- | --- |
| Metadatenmodell + eigene DSL | stabile Feldschlüssel, Allowlist und fachlich begrenzte Suche |
| Hot Chocolate GraphQL | neues UI, variable Datenansichten, mehrere relationale Ebenen |
| ASP.NET Core OData 8 | REST-Clients, URL-basierte Query-Sprache, bekannte Standards |

Die UI übermittelt keine Datenbankpfade, SQL oder freie LINQ-Ausdrücke. Das
Backend erzwingt Mandanten- und Zeilenrechte, validiert die Feldkonfiguration
und begrenzt Navigationstiefe, Paging und Kosten. EF Core bleibt darunter die
Datenzugriffsschicht, nicht die Query-Sprache für Clients.

## Trade-offs and risks

Expose niemals automatisch das gesamte EF-Modell. Jede Relation, jedes Feld und
jeder Operator braucht eine Allowlist; Root-Queries erzwingen Zeilenrechte und
Mandantentrennung. Pagination, maximale Seitengröße, Tiefen-/Kostenlimits,
Indizes für erlaubte Filter und Schutz gegen N+1 sind Pflicht.

„Transitiv“ bedeutet eine explizit begrenzte Navigationstiefe, nicht eine
unendliche Rekursion über den gesamten Graphen.

## Open questions

Offen sind insbesondere Wiederverwendung der Felddefinitionen je Root-Entity,
Collection-Semantik (`Any`/`All`), Version-1-Operatoren und das Rückgabeformat
für dynamische Spalten.

## Sources

- [[_raw/research/dotnet-transitive-query-api--shallow/report]]
- [[_raw/conversations/2026-08-26--filter-metadata-model-first]]
- [[_raw/conversations/2026-08-26--metadata-driven-relational-query-builder]]
