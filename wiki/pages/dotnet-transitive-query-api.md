---
title: ".NET: variable Query-API über Entitätsbeziehungen"
type: research-report
tags: [research, dotnet, api, graphql, odata, entity-framework]
state: draft
created: 2026-08-26
sources:
  - "_raw/research/dotnet-transitive-query-api--shallow/report.md"
---

# .NET: variable Query-API über Entitätsbeziehungen

## Conclusion

Für eine Hauptentität mit frei wählbaren Feldern und Filtern über mehrere
FK-/Navigationsstufen ist **GraphQL mit Hot Chocolate auf EF Core** die beste
Standardlösung. Der Client wählt die Rückgabeform; Hot Chocolate liefert
generierte, typsichere Filter für verschachtelte Objekte und Collections und
übersetzt sie für `IQueryable`.

**OData 8** ist die passende REST-Alternative, wenn `$filter`, `$select` und
`$expand` als standardisierte URL-Sprache erwünscht sind. Eine eigene
JSON-Filter-DSL erst bauen, wenn die erlaubten Suchszenarien fachlich eng und
stabil sind.

## Evidence

| Wahl | Wann |
| --- | --- |
| Hot Chocolate GraphQL | neues UI, variable Datenansichten, mehrere relationale Ebenen |
| ASP.NET Core OData 8 | REST-Clients, URL-basierte Query-Sprache, bekannte Standards |
| eigene DSL | feste, bewusst begrenzte Suche und keine externe Query-Sprache |

Beide fertigen Optionen unterstützen Feldselektion, relationale Ausgabe,
Filterung, Sortierung und Paging. EF Core bleibt darunter die
Datenzugriffsschicht, nicht die Query-Sprache für Clients.

## Trade-offs and risks

Expose niemals automatisch das gesamte EF-Modell. Jede Relation, jedes Feld und
jeder Operator braucht eine Allowlist; Root-Queries erzwingen Zeilenrechte und
Mandantentrennung. Pagination, maximale Seitengröße, Tiefen-/Kostenlimits,
Indizes für erlaubte Filter und Schutz gegen N+1 sind Pflicht.

„Transitiv“ bedeutet eine explizit begrenzte Navigationstiefe, nicht eine
unendliche Rekursion über den gesamten Graphen.

## Open questions

Entscheidend für die konkrete Wahl sind API-Kunden, DB/EF-Core-Version,
Berechtigungen und ob Abfragepfade wirklich ad hoc oder nur konfigurierbar sein
sollen.

## Sources

- [[_raw/research/dotnet-transitive-query-api--shallow/report]]

