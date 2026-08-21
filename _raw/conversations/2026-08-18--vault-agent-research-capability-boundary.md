---
title: "Vault-Agent: Recherchefähigkeit und Zugriffsgrenze"
type: raw-conversation
tags: [conversation, ai-assistant, agent, research, mcp, vault]
origin: codex conversation
created: 2026-08-18
---

# Vault-Agent: Recherchefähigkeit und Zugriffsgrenze

## Initial question

Der vorgeschlagene Hermes-Vault-Agent hat zunächst nur Lesezugriff. Es wurde
klargestellt, dass er dennoch Recherchen ausführen muss.

## Consensus / current state

Der Lesezugriff bezieht sich ausschließlich auf den lokalen Markdown-Vault:
der Agent darf ihn über den Wiki-MCP abfragen, aber nicht frei im Dateisystem
lesen oder schreiben. Für externe Recherche benötigt der Agent zusätzlich ein
eng begrenztes Recherchewerkzeug, etwa einen getrennten Such-/Abruf-MCP. Das
Werkzeug muss weder Vault-Schreibrechte noch Shell-, Browserautomation- oder
Infrastrukturrechte erhalten.

Die Auswahl des konkreten Rechercheanbieters, die zulässigen Quellen und der
Umgang mit Rechercheergebnissen sind noch offen. Ergebnisse bleiben zunächst
unreviewtes Raw-Material und werden erst durch menschliche Kuratierung zu
Wissen im Vault.

## Open questions

- Welcher Such-/Abrufdienst oder lokale Adapter ist für den privaten Agenten
  zulässig und wie wird dessen Credential verwaltet?
- Darf der Agent Webinhalte nur zusammenfassen oder auch als Raw-Research-
  Bericht ablegen?
- Welche Quellen-, Datenschutz- und Kostenregeln gelten für Modellanbieter und
  Webrecherche?

## Related Wiki pages

- [[target-network-and-operations-topology]]
- [[_raw/research/hermes-agent-alternatives/report]]
