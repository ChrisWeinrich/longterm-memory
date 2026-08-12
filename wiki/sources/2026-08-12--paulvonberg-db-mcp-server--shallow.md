---
title: "PaulvonBerg db-mcp-server: Shallow Research"
type: shallow-research
tags: [research, mcp, deutsche-bahn, mobility]
state: accepted
created: 2026-08-12
---

# PaulvonBerg db-mcp-server: Shallow Research

## Conclusion

`PaulvonBerg/db-mcp-server` ist ein öffentliches, unabhängiges Python-MCP für
Deutsche-Bahn- und Mobilitätsdaten. Es bündelt vier DB-APIs (Stationen,
Fahrpläne/Störungen, Parken sowie Aufzüge/Rolltreppen) in 13 Tools, sieben
Prompts und fünf Ressourcen. Der angegebene öffentliche Server ist jedoch
stillgelegt; sinnvoll ist deshalb nur ein eigener Betrieb mit eigenen
DB-API-Zugangsdaten.

Für eine kurzfristige persönliche Evaluation ist das Projekt als
Referenz/Prototyp brauchbar, aber nicht als sofort vertrauenswürdige
Produktivintegration: Die Entwicklung war klein (drei Commits), der letzte
Push datiert vom 2026-01-06, es gibt einen offenen, unbeantworteten
Session-Fehler, und die Abhängigkeiten sind nicht versioniert. Vor Nutzung
sollten lokale Tests, eine aktuelle MCP-Client-Prüfung und eine Prüfung der
DB-API-Lizenz- und Attributionspflichten erfolgen.

Die praktikabelste Alternative ist ein kleiner, lokaler MCP-Adapter direkt auf
den offiziellen DB-APIs: Er benötigt zwar ebenfalls den kostenlosen
Marketplace-Zugang und dessen Schlüssel, vermeidet aber die Wartungs- und
Transportaltlasten dieses Projekts. Für reine Reiseplanung/-abfahrten gibt es
unoffizielle HAFAS-/Vendo-Adapter und öffentliche `transport.rest`-Endpoints;
sie decken aber nicht gleichwertig Parken und Barrierefreiheit ab und haben
eigene Verfügbarkeits- und Nutzungsrisiken.

## Evidence

### Projekt und Reife

- Öffentliches Python-Repository, erstellt am 2025-07-24; GitHub meldet 18
  Stars, drei Forks, einen offenen Issue und ein Release `v1.0.0` (Tag
  `release`, veröffentlicht am 2025-08-08). Der API-Stand wurde am
  2026-08-12 abgefragt.
- Es gibt lediglich drei Commits. Der jüngste (`74852f7`, 2026-01-06) ersetzt
  die zuvor angebotene Server-URL durch einen Hinweis auf die Stilllegung.
- Der einzige offene Issue berichtet, dass `initialize` zwar funktioniert,
  danach aber `tools/list` und `tools/call` mit fehlender Session-ID scheitern;
  er hat keine Kommentare. Das ist ein konkretes Kompatibilitätsrisiko für
  direkte HTTP-Clients, nicht zwingend ein Fehler bei allen MCP-Clients.

### Technik und Funktion

- Der Server nutzt Python 3.11+, FastAPI, das Paket `mcp`, Pydantic, Uvicorn,
  HTTPX und Google Secret Manager. Die `requirements.txt` nennt keine
  Versionsbeschränkungen; damit ist der heutige reproduzierbare
  Abhängigkeitsstand nicht festgelegt.
- Aufbau: FastAPI-Einstieg (`main.py`), MCP-Registrierung, Pydantic-Modelle,
  Tool-Module für Stationen, Fahrpläne, Parken und Barrierefreiheit sowie
  Ressourcen und Prompts. Das Docker-Image basiert auf `python:3.11-slim`,
  exponiert Port 8080 und startet Uvicorn.
- Datenfunktionen: Stationssuche per Name/Koordinaten; geplante Abfahrten und
  Ankünfte; jüngste und vollständige Störungsmeldungen; Parkplätze und
  Prognosen; Status von Aufzügen/Rolltreppen und Mobilitätszentralen.
- Lokaler Start laut Dokumentation: virtuelle Umgebung, `pip install -r
  requirements.txt`, `.env` aus `.env.example`, dann `python main.py`. Für
  Cloud Run können die Zugangsdaten über Google Secret Manager kommen.

### Betrieb, Daten und Lizenz

- Erforderlich sind `DB_API_KEY` und `DB_API_SECRET` vom DB API Marketplace.
  Sie dürfen nicht in MCP-Konfigurationen oder im Repository landen. Der Code
  liest sie lokal aus `.env`, in GCP aus Secret Manager.
- Verwendet werden StaDa v2, Timetables v1, Parking Information v2 und FaSta
  v2. Das Projekt ist ausdrücklich nicht offiziell mit der Deutschen Bahn
  verbunden.
- Der Code steht unter CC BY 4.0, nicht unter einer typischen
  Software-Permissivlizenz wie MIT. Zusätzlich gelten die Lizenzbedingungen
  der zugrunde liegenden DB-Daten. Für Parkdaten nennt das Projekt dl-de/by-2-0
  mit vorgeschriebener Attribution und einem Verbot inhaltlicher Änderungen.

### Kosten und Alternativen

- Die Registrierung beim DB Kundenkonto und DB API Marketplace ist laut dessen
  Nutzungsbedingungen kostenlos. Die Bedingungen verweisen jedoch für
  Nutzungsrechte auf die jeweilige API-Lizenz, erlauben der DB
  Aufrufbeschränkungen und erlauben Änderungen oder die Einstellung von
  Angeboten. „Kostenloser Key“ ist daher für den privaten Einstieg richtig,
  aber keine Zusage für unbegrenzte oder dauerhaft unveränderte Nutzung.
- **Direkter offizieller Adapter (empfohlen):** Ein schlanker, lokaler MCP nur
  für die benötigten offiziellen Endpoints. Er behält die zuverlässigste
  Herkunft für Stationen, Fahrpläne, Störungen, Parken und FaSta bei und hält
  Credentials im lokalen Secret Store statt bei einem Drittanbieter.
- **`db-vendo-client` plus eigener Adapter:** Aktives JavaScript-Projekt für
  die neuen DB Vendo/Movas-Schnittstellen; es kann Reisen, Stationen, Abfahrten
  und Fahrten liefern. Der Maintainer weist aber darauf hin, dass für die
  Nutzung der DB-Schnittstellen streng genommen eine Erlaubnis nötig ist und
  nicht alle Daten verfügbar sind.
- **`v6.db.transport.rest` / `db-rest`:** Öffentliches, entwicklerfreundliches
  REST-Angebot für Reiseplanung und Abfahrten; kein eigener DB-Key nötig. Der
  alte DB-HAFAS-Endpoint wurde laut Projekt dauerhaft abgeschaltet; der
  Ersatz-Backend hat niedrigere Limits und nicht alle Funktionen. Nicht für
  kritische Automatisierung oder die Park-/Barrierefreiheitsfunktionen des
  ursprünglichen MCPs voraussetzen.
- **Generische API-zu-MCP-Gateways:** Sie können REST-OpenAPI-Schnittstellen
  als MCP bereitstellen. Sie sparen Implementierungsarbeit, vergrößern aber
  die Angriffsfläche und bringen keine DB-spezifische Datenmodellierung oder
  Rechtssicherheit mit.

## Trade-offs and risks

- **Verfügbarkeit:** Kein betreuter Endpoint; Selbsthosting, Monitoring und
  Kosten liegen beim Betreiber.
- **MCP-Kompatibilität:** Der offene Session-Issue und die alte
  `mcp-remote`-Anleitung lassen offen, ob aktuelle Streamable-HTTP-Clients
  ohne Anpassung funktionieren.
- **Sicherheit:** Die README nennt Rate Limiting, Input Validation und Security
  Headers. Das ersetzt keine eigene Prüfung von Authentisierung, Netzwerk-
  Exposition, Abhängigkeiten und Secret-Handling vor einem Internetbetrieb.
- **Datenrecht:** Ergebnisse, insbesondere Parkdaten, dürfen nicht beliebig
  gespeichert, verändert oder weitergegeben werden. Die aktuellen offiziellen
  DB-Bedingungen sollten vor einer Integration separat geprüft werden.
- **Wartung:** Die geringe Commit-Historie und unpinnte Dependencies erhöhen
  das Risiko von Bitrot gegenüber aktuellen Python- und MCP-Versionen.

## Open questions

- Funktioniert die aktuelle `main`-Version mit Codex/Claude über heutigen
  Streamable-HTTP-Transport und korrekte Session-Aushandlung?
- Sind alle vier DB-APIs mit neuen Zugangsdaten weiterhin verfügbar und für den
  konkreten persönlichen Zweck zulässig?
- Welche Authentisierung und Netzwerkbegrenzung soll ein eigener Endpunkt
  erhalten, falls er nicht ausschließlich lokal über stdio läuft?
- Ist direkte Nutzung der offiziellen DB-Schnittstellen mit einem kleineren,
  lokalen Adapter langfristig wartungsärmer?

## Sources

- [GitHub repository and README](https://github.com/PaulvonBerg/db-mcp-server)
  — Funktionen, Architektur, Setup, Stilllegungs-Hinweis, DB-APIs und
  Lizenzhinweise; abgerufen 2026-08-12.
- [GitHub repository metadata API](https://api.github.com/repos/PaulvonBerg/db-mcp-server)
  — Erstellungs-, Aktivitäts- und Popularitätsdaten; abgerufen 2026-08-12.
- [Commit history](https://github.com/PaulvonBerg/db-mcp-server/commits/main)
  — drei Commits und Stilllegungs-Commit; abgerufen 2026-08-12.
- [Open issue #3](https://github.com/PaulvonBerg/db-mcp-server/issues/3) —
  berichteter Session-ID-Fehler; abgerufen 2026-08-12.
- [requirements.txt](https://github.com/PaulvonBerg/db-mcp-server/blob/main/requirements.txt),
  [Dockerfile](https://github.com/PaulvonBerg/db-mcp-server/blob/main/Dockerfile),
  [config.py](https://github.com/PaulvonBerg/db-mcp-server/blob/main/config.py)
  und [LICENSE](https://github.com/PaulvonBerg/db-mcp-server/blob/main/LICENSE)
  — Abhängigkeiten, Deployment, Secrets und Lizenz; abgerufen 2026-08-12.
- [DB API Marketplace – Nutzungsbedingungen](https://developers.deutschebahn.com/db-api-marketplace/apis/nutzungsbedingungen)
  — kostenlose Registrierung, API-spezifische Lizenzen, Limits und
  Änderungsrechte; abgerufen 2026-08-12.
- [DB Timetables API](https://developers.deutschebahn.com/db-api-marketplace/apis/product/timetables/api/160160)
  — offizielle Authentifizierung mit Client-ID und API-Key; abgerufen
  2026-08-12.
- [db-vendo-client](https://github.com/public-transport/db-vendo-client) und
  [db-rest](https://github.com/derhuerst/db-rest) — unoffizielle Alternativen,
  Funktionsumfang und Einschränkungen; abgerufen 2026-08-12.
- [transport.rest](https://transport.rest/) — öffentliche Transit-Endpoints;
  abgerufen 2026-08-12.
