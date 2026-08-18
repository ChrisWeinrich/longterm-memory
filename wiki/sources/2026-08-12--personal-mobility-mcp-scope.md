---
title: "Persönliches Mobility-MCP: Fahrpläne, Abfahrten und Störungen"
type: discussion
tags: [deutsche-bahn, vvs, mobility, mcp, infrastructure]
state: draft
created: 2026-08-12
---

# Persönliches Mobility-MCP: Fahrpläne, Abfahrten und Störungen

## Ziel

Ein schönes, kleines persönliches Tool für Agenten, um Reise- und
Mobilitätsinformationen anzuschauen — mit Schwerpunkt auf Fahrplänen,
Abfahrten und Störungen. Es läuft lokal als read-only MCP über stdio und ist
kein öffentlicher Dienst.

## Beschlossener erster Umfang

- **DB-Station suchen:** Bahnhof anhand eines Namens finden und die passende
  Stationskennung auflösen.
- **Abfahrtstafel:** nächste Abfahrten und Ankünfte an einem DB-Bahnhof, mit
  aktuellen Änderungen gegenüber dem Sollfahrplan.
- **Fahrplan-/Zugdetails:** den relevanten Fahrplanausschnitt und bekannte
  Abweichungen für eine Station anzeigen.
- **Lokaler ÖPNV (VVS):** Haltestellen, Linien und Soll-Fahrpläne im Raum
  Stuttgart/Ludwigsburg aus den VVS-OpenData-Datensätzen; Echtzeit-Abfahrten
  erst nach Freischaltung der VVS-TRIAS- oder GTFS-Realtime-API.

Für den Anfang bewusst **nicht** enthalten: Ticketkauf, Konto- oder
Zahlungsfunktionen, schreibende API-Aufrufe, öffentlich erreichbarer
Netzwerkbetrieb und eine allgemeine Tür-zu-Tür-Routenplanung über inoffizielle
DB-Endpunkte.

## Datenquellen und Zugang

| Bedarf | Vorgesehene Quelle | Zugang und Grenze |
| --- | --- | --- |
| DB-Abfahrten, Sollfahrplan, Abweichungen | DB Timetables API | kostenloser Plan, 60 Aufrufe/Minute; DB-Konto, Marketplace-Freischaltung und eigener Schlüssel nötig |
| DB-Bahnhofsdaten, später Parken/Barrierefreiheit | DB StaDa API | kostenloser Plan, 10 Aufrufe/Sekunde; API-Key pro Anwendung und Kunde |
| VVS-Haltestellen, Linien, Sollfahrplan | VVS OpenData | statische CSV-/GTFS-Datensätze; Lizenz vor Einbindung prüfen |
| VVS-Echtzeit | VVS TRIAS oder GTFS Realtime | Vorhaben kurz an `opendata@vvs.de` beschreiben und API-Nutzungsvereinbarung prüfen |

Der kostenlose Einstieg genügt für den Startumfang. Es ist kein kostenpflichtiger
DB-Plan erforderlich. Kostenpflichtige DB-Produkte wie RIS::Stations gehören
nicht in diese erste Ausbaustufe.

## Umsetzung und Sicherheit

- Eigenen, schlanken Adapter direkt auf die offiziellen APIs bauen; nicht den
  stillgelegten gehosteten Server von Paul von Berg übernehmen. Dessen
  öffentlicher Endpoint ist eingestellt; zudem sprechen geringe Wartungsaktivität
  und ein offener Session-Fehler gegen eine direkte Produktivübernahme.
- Ausschließlich lokale stdio-Anbindung; kein HTTP-Listener und keine
  Fernfreigabe.
- Schlüssel nicht im Repository oder in MCP-Client-Konfigurationen ablegen,
  sondern im bestehenden Secret-Workflow verwalten.
- API-spezifische Lizenz-, Nutzungs- und Attributionspflichten vor dem
  produktiven Einsatz erneut prüfen; Limits und Verfügbarkeit können sich
  ändern.
- Tests für Tool-Ausgaben und die verwendeten MCP-Clients vor der täglichen
  Nutzung ergänzen.

## Live-Bus-POC: Was noch benötigt wird

Die vorhandene Planung reicht als Architekturentscheidung, aber **noch nicht**
für echte Bus-Abfahrten in Echtzeit. DB Timetables ist für DB-Bahnhöfe gedacht;
die Live-Abfahrten eines lokalen VVS-Busses müssen über die VVS-TRIAS- oder
GTFS-Realtime-API kommen.

Für einen minimalen POC benötigen wir daher nur:

1. Eine kurze Anfrage an `opendata@vvs.de` mit dem Vorhaben „persönlicher,
   lokaler read-only MCP; Live-Abfahrten einzelner VVS-Haltestellen; keine
   Weitergabe und keine Serienabfragen“.
2. Die daraufhin bereitgestellten Zugangsdaten und technische Dokumentation;
   beides in den bestehenden Secret-Workflow übernehmen, nicht ins Repository.
3. Die konkrete Haltestelle beziehungsweise Halteposition deines Busses und
   eine kleine Tool-Antwort: Linie, Ziel, planmäßige und prognostizierte
   Abfahrtszeit, Verspätung sowie Ausfall-/Störungshinweise.
4. Eine Abfrage nur auf Nutzerwunsch oder mit konservativem Caching. Die
   VVS-Nutzungsvereinbarung erlaubt Live-Einzelabfragen, untersagt aber
   systematische Serienabfragen und fordert Quellhinweis/Haftungshinweis bei
   einer angezeigten Anwendung.

Statisches VVS-GTFS ist trotzdem nützlich, um Haltestellen und Linien offline
aufzulösen; es ersetzt keine Echtzeit-Prognose. Eine allgemeine
Tür-zu-Tür-Reiseplanung ist ausdrücklich nicht Teil dieses POC.

## Verworfene Alternativen

- Das externe `PaulvonBerg/db-mcp-server` dient höchstens als Funktionsreferenz;
  es wird nicht betrieben oder übernommen.
- Unoffizielle DB-HAFAS-/Vendo-Adapter und öffentliche Transit-Endpunkte werden
  für diesen POC nicht verwendet: Sie sind keine verlässliche Grundlage für den
  vollständigen lokalen Bus- und Störungsumfang und haben eigene Nutzungs- und
  Verfügbarkeitsrisiken.
- Kostenpflichtige DB-Produkte wie RIS::Stations sind für den gewählten Umfang
  nicht nötig.

## Vorgeschlagene Werkzeuge

1. `find_station(query)` — DB-Station oder VVS-Haltestelle suchen.
2. `departures(stop, when?, limit?)` — nächste Abfahrten mit Verspätung,
   Gleis und Hinweis auf Änderungen.
3. `station_board(station, when?)` — DB-Ankünfte, Abfahrten und relevante
   Fahrplanabweichungen.
4. Später: `station_facilities(station)` für Barrierefreiheit, Parken und
   Öffnungszeiten; `vvs_realtime_departures(stop)` erst nach VVS-Freischaltung.

## Offene Entscheidungen

- Soll die erste Version nur DB-Timetables umsetzen und VVS als zweite Phase
  folgen, oder beide Quellen von Anfang an unterstützen?
- Welche Ausgabe ist am nützlichsten: eine kompakte Abfahrtstafel, strukturierte
  Rohdaten oder beides?
- Soll eine reine persönliche Ansicht künftig durch Benachrichtigungen ergänzt
  werden? Das wäre ein separater, späterer Umfang.

## Quellen

- [DB API Marketplace: Timetables](https://developers.deutschebahn.com/db-api-marketplace/apis/product/timetables) — kostenloser Plan, Limits und Lizenz; abgerufen 2026-08-12.
- [DB API Marketplace: StaDa – Station Data](https://developers.deutschebahn.com/db-api-marketplace/apis/product/stada) — Stationdaten, kostenloser Plan und Key-Vorgaben; abgerufen 2026-08-12.
- [DB API Marketplace: Nutzungsbedingungen](https://developers.deutschebahn.com/db-api-marketplace/apis/nutzungsbedingungen) — kostenlose Registrierung und Freischaltung; abgerufen 2026-08-12.
- [VVS OpenData](https://www.opendata-oepnv.de/ht/de/organisation/verkehrsverbuende/vvs/startseite) — Haltestellen, Linien, GTFS und Zugang zu Echtzeitdaten; abgerufen 2026-08-12.
- [VVS Apps & Dienste](https://www.vvs.de/service/apps-dienste) — VVS-OpenData und vorhandene Echtzeit-Angebote; abgerufen 2026-08-12.
- [VVS API-Nutzungsvereinbarung](https://www.opendata-oepnv.de/ht/de/standards/nutzungsvereinbarung-api) — Live-Abfragen, Weitergabe, Kennzeichnung und Lastbegrenzung; abgerufen 2026-08-12.
- [PaulvonBerg/db-mcp-server](https://github.com/PaulvonBerg/db-mcp-server) — frühere Funktionsreferenz und Stilllegungs-Hinweis; abgerufen 2026-08-12.
