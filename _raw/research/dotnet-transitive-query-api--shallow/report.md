---
title: ".NET: variabel filternde und projizierende API über Entitätsbeziehungen – Kurzrecherche"
type: raw-research-report
tags: [research, dotnet, api, graphql, odata, entity-framework]
origin: research-workflow
created: 2026-08-26
---

# .NET: variabel filternde und projizierende API über Entitätsbeziehungen – Kurzrecherche

## Conclusion

Der Wunsch entspricht einer **querybaren Daten-API**, nicht einem einzelnen
CRUD-Endpunkt: Eine Hauptentität wird abgefragt, Filter dürfen über beliebige
freigegebene Navigationen/FKs gehen, und der Client bestimmt die benötigte
Ausgabeform.

Die passendste fertige .NET-Lösung ist **GraphQL mit Hot Chocolate und EF
Core**. GraphQL liefert variablen Output nativ über das Selection Set; Hot
Chocolate generiert typsichere Filter für Skalare, verschachtelte Objekte und
Collections und kann sie auf `IQueryable` in Datenbankabfragen übersetzen. Es
eignet sich besonders für eine Anwendung mit variablen Screens und komplexen,
mehrstufigen Relationen.

Wenn die API bewusst REST bleiben soll und eine standardisierte URL-Sprache
erwünscht ist, ist **ASP.NET Core OData 8** die direkte Alternative:
`$filter`, `$select` und `$expand` decken Filterung, Feldauswahl und relationale
Ausgabe ab.

Eine selbst erfundene JSON-Filter-DSL sollte erst gewählt werden, wenn nur ein
kleiner, fachlich kontrollierter Satz von Queries erlaubt sein soll. Sie kostet
mehr Implementierungs- und Sicherheitsarbeit als GraphQL/OData.

## Evidence

| Ansatz | Variabler Output | Filter über FK-/Navigationsketten | Geeignet für |
| --- | --- | --- | --- |
| GraphQL + Hot Chocolate | ja, Client wählt Felder und verschachtelte Objekte | ja; verschachtelte Objektfilter sowie `some`/`all`/`none` für Collections | neue, UI-getriebene API; komplexe Abfragen |
| ASP.NET Core OData 8 | ja, `$select` und `$expand` | ja, über OData-Navigationen und Filterausdrücke | REST-Ökosystem, BI-/Admin-Clients, bekannte URL-Semantik |
| eigene Filter-DSL auf EF Core | nur nach eigener Umsetzung | ja, durch geparste, allow-gelistete Expression Trees | eng definierte fachliche Suche mit stabiler öffentlicher Oberfläche |

### GraphQL / Hot Chocolate

Hot Chocolate erstellt Filtertypen aus .NET-Modellen. Für Referenzen können
Filter geschachtelt werden; für Collections unterstützt es `some`, `all`,
`none` und `any`. Beispiel für eine Hauptentität `Customer`, gefiltert über
zwei Beziehungsebenen, bei frei gewählter Ausgabe:

```graphql
query {
  customers(
    where: {
      orders: { some: { lineItems: { some: { product: { category: { name: { eq: "Bikes" } } } } } } }
    }
  ) {
    id
    name
    orders { id lineItems { quantity product { sku name } } }
  }
}
```

Die genaue Syntax hängt vom Schema ab, aber das Muster erfüllt die Anforderung:
Root-Entity suchen, transitiv über Navigationspfade filtern und nur die
benötigten Felder zurückgeben. Die Projektionen bauen aus dem Selection Set eine
SQL-nahe Projektion; in aktueller Hot-Chocolate-Dokumentation bündelt
`QueryContext<T>` Filter, Sortierung und Projektion auf einem `IQueryable`
([Filter](https://chillicream.com/docs/hotchocolate/fetching-data/filtering),
[Projektionen](https://chillicream.com/docs/hotchocolate/fetching-data/projections)).

### OData

OData 8 bietet in ASP.NET Core `$filter`, `$select`, `$expand`, `$orderby`,
`$top` und `$skip`. Beispiel:

```text
GET /odata/Customers?
  $filter=Orders/any(o: o/LineItems/any(i: i/Product/Category/Name eq 'Bikes'))&
  $select=Id,Name&
  $expand=Orders($select=Id;$expand=LineItems($select=Quantity;$expand=Product($select=Sku,Name)))
```

Die URL ist länger, aber sehr standardisiert und gut für Clients, die REST und
Query-Parameter erwarten. Microsoft demonstriert `$select`, `$expand` und
Filter innerhalb expandierter Beziehungen; pro Endpoint können erlaubte
Query-Optionen eingeschränkt werden
([Microsoft Learn: Query Options](https://learn.microsoft.com/en-us/odata/webapi-8/fundamentals/query-options)).

### EF Core ist die Datenzugriffsschicht, nicht die öffentliche Query-Sprache

EF Core kann Beziehungen mit `Include` und `ThenInclude` über mehrere Ebenen
laden. Das ist nützlich für fest definierte Serverqueries, aber keine gute
unmittelbare API-Sprache für untrusted Clients. Microsoft warnt zudem, dass das
Eager-Loading von Collections in einer einzigen Query Performanceprobleme
verursachen kann
([Microsoft Learn: Related Data](https://learn.microsoft.com/en-us/ef/core/querying/related-data/eager)).

## Trade-offs and risks

- **Nicht die Datenbank freigeben:** Keine generische Eingabe direkt als LINQ,
  SQL oder vollständiges EF-Modell ausführen. Exponierte Typen, Felder,
  Relationen und Operatoren sind allow-gelistet; DTOs/GraphQL-Typen trennen das
  API-Modell vom Persistenzmodell.
- **Autorisierung vor Abfrage:** Zeilenrechte müssen in jedem Root-Query in
  `IQueryable` eingeschränkt werden. Feldrechte und Mandantentrennung dürfen
  nicht erst nach dem Laden erfolgen.
- **Kosten begrenzen:** pagination verpflichtend, maximale Seitengröße und
  maximale Expand-/Graph-Tiefe setzen; Sortierung nur auf indizierten Feldern;
  Query-Timeout und Beobachtbarkeit einrichten. OData bietet optionale
  Begrenzungen wie `AllowedQueryOptions` und `SetMaxTop`; GraphQL benötigt
  Paging, Depth-/Cost-Limits und DataLoader gegen N+1.
- **Zyklen bewusst behandeln:** „Transitiv über die ganze Datenbank“ darf nicht
  unbeschränkt heißen. Erlaubte Navigationspfade und maximale Tiefe gehören in
  das API-Design.
- **Rückgabemodelle stabil halten:** Entity-Graphen direkt serialisieren kann
  Zyklen, versteckte Felder und Breaking Changes erzeugen.

## Open questions

- Ist der Endpoint nur für ein eigenes Frontend oder öffentlich für Dritte?
- Welche Datenbank und welche EF-Core-Version werden verwendet?
- Gibt es Mandanten-, Rollen- oder Feldberechtigungen?
- Braucht der Client ad-hoc beliebige Pfade oder nur bekannte Suchszenarien?

## Sources

- Hot Chocolate Filtering: https://chillicream.com/docs/hotchocolate/fetching-data/filtering
- Hot Chocolate Projections: https://chillicream.com/docs/hotchocolate/fetching-data/projections
- ASP.NET Core OData 8 Query Options:
  https://learn.microsoft.com/en-us/odata/webapi-8/fundamentals/query-options
- EF Core eager loading:
  https://learn.microsoft.com/en-us/ef/core/querying/related-data/eager

