---
title: "Hermes Agent und Alternativen — Rechercheplan"
type: research-plan
tags: [research, ai-assistant, agent, mcp, tailscale, obsidian]
state: accepted
created: 2026-08-18
---

# Hermes Agent und Alternativen

## Question

Ist Hermes Agent für den ersten privaten Vault-Agenten die passendste Runtime,
oder bietet LibreChat, Letta, Open WebUI oder eine schlanke Eigenarchitektur
einen klaren Vorteil bei gleichem Sicherheits- und Betriebsziel?

## Decision and audience

Entscheidungsvorlage für Christian: Auswahl einer Runtime für einen privaten,
über Tailscale erreichbaren Vault-Agenten. Der MVP beantwortet ausschließlich
Wissens- und Auftragsfragen; er führt keine externen oder
Infrastrukturaktionen aus.

## Scope

- Hermes Agent als Referenz: Dashboard/Gateway, MCP-Client und -Server,
  Sitzungen, Profile, Updates und Sicherung.
- LibreChat, Letta und Open WebUI: Self-Hosting, Authentifizierung,
  MCP-/Agenten-Schnittstellen, Speicher- und Betriebsmodell.
- Eine schlanke Eigenarchitektur aus Agent SDK und kleinem Web-/MCP-Adapter
  nur als Kontroll- und Kostenreferenz.
- Für jede Option: Tailscale-Zugang, Berechtigungsgrenzen, Datenfluss zu
  Modellanbietern, API/Sitzungen/Auftragsstatus/Logging sowie Migration aus
  dem bestehenden Markdown-/Wiki-MCP-Template.
- Abnahmefälle: kein freier Vault-Dateizugriff; bestehender Wiki-MCP bleibt
  die Vault-Grenze; Obsidian bleibt vollständig nutzbar; Hermes oder eine
  gleichwertig enge Alternative kann per MCP angesprochen werden.

## Exclusions

- Kein Produktiv-Rollout, keine Modell- oder Anbieterwahl und keine
  Infrastrukturänderung.
- Keine Bewertung autonomer Agenten, Messaging-Kanäle oder Schreib-/Exec-Tools
  für den MVP.
- Keine Übernahme von Agenten-Memory in den kuratierten Markdown-Vault.

## Success criteria

Der Raw-Bericht enthält ausschließlich belegte Aussagen, eine Quellenliste mit
offiziellen URLs und Abrufdatum, eine Vergleichsmatrix, klar getrennte
Inference, Risiken, einen minimalen Betriebsentwurf und eine begründete
Empfehlung inklusive Migrationspfad.
