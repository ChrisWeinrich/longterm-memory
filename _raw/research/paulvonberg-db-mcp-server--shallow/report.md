---
title: "PaulvonBerg db-mcp-server: Shallow Research"
type: raw-research-report
tags: [research, mcp, deutsche-bahn, mobility]
origin: legacy-wiki-draft
created: 2026-08-12
legacy_path: wiki/sources/2026-08-12--paulvonberg-db-mcp-server--shallow.md
---

# PaulvonBerg db-mcp-server: Shallow Research

## Conclusion

`PaulvonBerg/db-mcp-server` ist ein unabhängiges Python-MCP für DB-Daten. Der
öffentliche Server ist stillgelegt; für eine persönliche Nutzung ist daher nur
ein eigener Betrieb mit eigenen DB-API-Zugangsdaten sinnvoll. Das Projekt ist
als Funktionsreferenz brauchbar, nicht als direkt vertrauenswürdige
Produktivintegration: geringe Wartungsaktivität, ein offener Session-Fehler
und nicht gepinnte Abhängigkeiten erhöhen das Risiko.

Ein kleiner lokaler Adapter direkt auf offiziellen DB-APIs ist die bevorzugte
Alternative. Er braucht ebenfalls Marketplace-Zugang, vermeidet aber die
Wartungs- und Transportaltlasten des Fremdprojekts.

## Evidence

- Das Projekt bündelt Stationen, Fahrpläne/Störungen, Parken und
  Barrierefreiheit; es verwendet Python, FastAPI, MCP, Pydantic, Uvicorn und
  HTTPX.
- Der öffentliche Endpoint wurde eingestellt; ein offener Issue beschreibt
  einen Session-ID-Fehler nach erfolgreicher Initialisierung.
- DB-Zugangsdaten gehören weder in MCP-Konfiguration noch ins Repository.
- DB-API-Lizenzen, Aufrufgrenzen und Attributionspflichten bleiben vor Nutzung
  zu prüfen.

## Trade-offs and risks

- Selbstbetrieb bedeutet Verantwortung für Verfügbarkeit, Tests und
  Secret-Handling.
- Unoffizielle HAFAS-/Vendo-Adapter und öffentliche Transit-Endpunkte decken
  nicht zuverlässig den vollständigen vorgesehenen Funktionsumfang ab und
  haben eigene Nutzungs- und Verfügbarkeitsrisiken.

## Sources

- https://github.com/PaulvonBerg/db-mcp-server
- https://api.github.com/repos/PaulvonBerg/db-mcp-server
- https://github.com/PaulvonBerg/db-mcp-server/issues/3
- https://developers.deutschebahn.com/db-api-marketplace/apis/nutzungsbedingungen
