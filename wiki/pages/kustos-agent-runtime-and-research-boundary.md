---
title: "Kustos-Agent: Runtime und Recherchegrenze"
type: research-report
tags: [ai-assistant, agent, hermes, mcp, tailscale, research]
state: draft
created: 2026-09-12
sources:
  - "_raw/research/hermes-agent-alternatives/report.md"
  - "_raw/conversations/2026-08-18--vault-agent-research-capability-boundary.md"
---

# Kustos-Agent: Runtime und Recherchegrenze

## Conclusion

Hermes Agent ist die bevorzugte Runtime für einen engen, selbst gehosteten
Kustos-MVP: authentifiziert im Tailnet, mit dem Wiki MCP als Wissensgrenze und
ohne freien Datei-, Shell-, Browser- oder Infrastrukturzugriff. Ein Lesezugriff
auf Kustos schließt externe Recherche nicht aus, benötigt dafür aber ein
separates, eng begrenztes Such-/Abrufwerkzeug.

Rechercheergebnisse bleiben zunächst Raw-Material; nur menschliche Curation
macht daraus Kustos-Wissen.

## Evidence

- Hermes bietet Gateway/Dashboard, MCP-Client, Profile und Sitzungen; bei
  nicht-lokalem Binden verlangt seine Dokumentation Authentifizierung.
- Der Wiki MCP darf nur seine kontrollierten Wissenswerkzeuge freigeben; keine
  Runtime schreibt direkt in `wiki/pages/`.
- LibreChat, Letta, Open WebUI und eine schlanke Eigenarchitektur bleiben
  Alternativen, haben für den engen MVP aber keinen klaren Vorteil.

## Trade-offs and risks

Tailnet-Zugang ersetzt keine Anwendungsauthentifizierung. Sessions und Logs
sind Laufzeitdaten, nicht kuratiertes Wissen. Modellzugang und Recherche-
Credentials bleiben außerhalb des Vaults.

## Open questions

- Welche Hermes-Version und welche Authentifizierung sollen eingesetzt werden?
- Wer im Tailnet darf den Agenten erreichen?
- Welcher Modellanbieter und welches Recherchewerkzeug sind für diese
  Datenklasse zulässig?
- Reicht synchroner Chat, oder entsteht ein tatsächlicher Bedarf für einen
  separaten Auftragsadapter?

## Sources

- [[_raw/research/hermes-agent-alternatives/report]]
- [[_raw/conversations/2026-08-18--vault-agent-research-capability-boundary]]
