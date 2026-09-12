---
title: 'Deep Research: Agent- und Config-Dashboard Markt'
type: external-note
tags:
- external
- deep-research
- agent-dashboard
- configuration
- mcp
- skills
- chezmoi
origin: wiki-mcp
received_at: '2026-09-12T10:19:42Z'
---

# Deep Research: Agent- und Config-Dashboard Markt

# Deep Research Brief: Agent- und Config-Dashboard

## Ziel

Eine Markt- und Tool-Recherche für einen privaten, lokal betriebenen Überblick über den aktuellen Agenten- und Konfigurationsstand des Macs.

## Ausgangslage

Die Soll-Konfiguration liegt im chezmoi-Repository. Sichtbar werden sollen vor allem Codex, Claude, Copilot und weitere Agenten: installierte Skills, MCP-Server, globale Anweisungen (z. B. AGENTS.md), effektive Konfiguration, Berechtigungen sowie Soll-/Ist-Drift.

## Forschungsfragen

1. Welche fertigen Open-Source- oder kommerziellen Agent-Dashboards existieren für Claude Code, Codex, Copilot, Cursor und vergleichbare Coding Agents?
2. Welche Werkzeuge visualisieren bzw. prüfen MCP-Server, Skills, Agent-Konfigurationen und Berechtigungen?
3. Welche Dotfiles-/chezmoi-nahen UIs, Browser-Viewer oder IDE-Erweiterungen eignen sich für Source-vs.-Live-Konfiguration?
4. Welche Kandidaten können lokal und privat betrieben werden?
5. Wo bleiben Lücken, die einen kleinen eigenen, read-only Dashboard-Collector rechtfertigen?

## Vergleichskriterien

- Agentenabdeckung und Konfigurationsinventar
- Skills, MCPs, Policies und effektive Berechtigungen
- lokaler/offline Betrieb und Netzwerkbindung
- Umgang mit Secrets und Redaction
- Integrationsaufwand mit chezmoi
- Reife, Lizenz und Wartbarkeit
- Eignung als Übernehmen, Kombinieren oder Referenz für einen eigenen schlanken Viewer

## Bekannte Ausgangspunkte

- MCP Inspector ist ein bestehendes Werkzeug für die Live-Inspektion einzelner MCP-Server, aber nicht zwingend ein gesamtes Agent-/Config-Inventar.
- JSONEditor und Monaco Editor sind mögliche Darstellungskomponenten für redigierte Konfigurationsbäume beziehungsweise Source-vs.-Live-Diffs.
- Die Recherche soll diese erste Einschätzung verifizieren oder korrigieren und den Markt breiter abdecken.

## Status

Unreviewter Research-Auftrag. Es wurden noch keine Kauf-/Build-Entscheidungen getroffen.

## Nächster Schritt

Explorative Deep Research durchführen und einen zitierten Vergleich mit klarer Empfehlung ergänzen.
