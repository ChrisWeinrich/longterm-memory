---
title: "Codebahn als europäische Forgejo- und Agentenplattform"
type: research-plan
tags: [research, codebahn, forgejo, ci-cd, mcp, cli, coding-agents, sovereignty]
state: accepted
created: 2026-10-01
---

# Codebahn als europäische Forgejo- und Agentenplattform

## Question

Eignet sich Codebahn als europäisch souveräner Ersatz für GitHub samt Repos,
Issues und CI/CD, und welche dokumentierten Schnittstellen gibt es für CLI,
MCP und Coding-Agenten?

## Decision and audience

Christian entscheidet, ob ein zeitlich begrenzter Pilot von Codebahn seinen
privaten Infrastruktur-Stack ersetzen oder ergänzen soll. Das Ergebnis ist
Entscheidungsmaterial, keine Beschaffung oder Produktivfreigabe.

## Scope

- Betreiber, Vertrag, Datenschutz, Subprozessoren, Datenstandorte, Exit und
  Reifeindikatoren.
- Standard-Forgejo-Funktionen sowie dokumentierte Abweichungen/Erweiterungen.
- CI/CD: Runner-Isolation, Workflow-Kompatibilität, Secrets, Registry,
  Deployments und Datenflüsse.
- Codebahn-Dokumentation, REST API, CLI und MCP: Authentisierung,
  Berechtigungen, Funktionsumfang und Eignung für lokale Coding Agents.
- Ob Codebahn selbst eine Coding-Agent-Laufzeit bereitstellt oder nur eine
  Integrationsoberfläche für externe Agenten hat.

## Exclusions

- Installation, Kontoerstellung, Migration oder verbindliche Beschaffung.
- Allgemeiner Vergleich aller Forgejo-Anbieter, außer bei notwendigen
  Einordnungen.
- Unbelegte Marketingaussagen als Tatsachen oder Rechtsberatung.

## Success criteria

- Jede wesentliche Aussage verweist auf offizielle Codebahn-, Forgejo- oder
  Vertragsdokumentation und ist als Fakt oder Inferenz markiert.
- Es gibt eine klare Pilot-Checkliste und Ausschlusskriterien.
- MCP/CLI/Agentenpfad ist konkret genug, um eine sichere erste lokale
  Integration zu bewerten.
