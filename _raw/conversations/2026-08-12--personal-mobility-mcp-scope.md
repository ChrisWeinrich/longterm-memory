---
title: "Persönliches Mobility-MCP: konsolidierter Umfang"
type: raw-conversation
tags: [deutsche-bahn, vvs, mobility, mcp, infrastructure]
origin: legacy-wiki-draft
created: 2026-08-12
legacy_path: wiki/sources/2026-08-12--personal-mobility-mcp-scope.md
---

# Persönliches Mobility-MCP: konsolidierter Umfang

## Consensus / current state

Das persönliche Mobility-MCP läuft lokal und read-only über stdio. Der erste
Umfang umfasst DB-Stationssuche, Abfahrtstafel sowie Fahrplan-/Zugdetails mit
bekannten Abweichungen. Für Stuttgart/Ludwigsburg kommen VVS-Haltestellen,
Linien und Soll-Fahrpläne aus OpenData hinzu; Echtzeitdaten erst nach
Freischaltung von VVS-TRIAS oder GTFS Realtime.

Der Adapter wird direkt gegen offizielle DB-APIs gebaut. Das externe
PaulvonBerg-MCP bleibt nur Funktionsreferenz. Es gibt keinen HTTP-Listener,
keine Fernfreigabe, keine schreibenden API-Aufrufe, keinen Ticketkauf und keine
allgemeine Tür-zu-Tür-Planung.

DB- und VVS-Zugangsdaten werden ausschließlich im Secret-Workflow geführt.
Lizenz-, Nutzungs- und Attributionspflichten sowie aktuelle Limits werden vor
produktivem Einsatz erneut geprüft.

## Decisions

- Start mit den Tools `find_station`, `departures` und `station_board`.
- VVS-Echtzeit erst nach expliziter Freischaltung und nur bedarfsorientiert
  beziehungsweise mit konservativem Caching abfragen.
- Kostenpflichtige DB-Produkte und inoffizielle Transit-Adapter gehören nicht
  in den ersten Umfang.

## Open questions

- DB-Timetables zuerst allein oder DB und VVS von Beginn an?
- Kompakte Abfahrtstafel, strukturierte Rohdaten oder beides?
- Spätere persönliche Benachrichtigungen als separater Umfang?
