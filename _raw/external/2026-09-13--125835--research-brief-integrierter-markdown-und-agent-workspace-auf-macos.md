---
title: 'Research Brief: Integrierter Markdown- und Agent-Workspace auf macOS'
type: external-note
tags:
- external
- research
- agent-workflow
- orchestration
- markdown
- obsidian
- neovim
- hunk
- yabai
- omarchy
- macos
origin: wiki-mcp
received_at: '2026-09-13T12:58:35Z'
---

# Research Brief: Integrierter Markdown- und Agent-Workspace auf macOS

# Research Brief: Integrierter Markdown- und Agent-Workspace auf macOS

## Ziel

Ein stabiler, lokaler Entwicklungs- und Wissensflow auf privatem und Business-Mac. Private Maschine zuerst; Business-Rollout erst nach bestandenem privaten Proof-of-Concept.

Die gewünschte Bedienung ist ein gemeinsamer Workspace-Kontext: Wenn eine Agent-Gruppe im gewählten Agent-Manager aktiviert wird, sollen die zugehörigen Werkzeuge im selben Kontext bereitstehen:

```text
Agent-Gruppe / workspace_id
  → Repository + aktiver Worktree
  → Obsidian: passender Vault + Plan, README, MOC oder Entscheidung
  → Neovim: gleicher Worktree
  → Hunk: gleicher lokaler Diff-Bereich
  → GitHub: Issue, Pull Request und CI
  → optional yabai: Fensteranordnung
```

Nicht jedes Werkzeug muss zwingend automatisch folgen. Eine erste, verlässliche Version darf ein explizit gestarteter Workspace-Launcher sein. Automatisches Folgen beim Gruppenwechsel ist nur sinnvoll, wenn die gewählte Agent-Steuerung dafür dokumentierte, lokale und sichere Hooks oder APIs hat.

## Ausgangslage und vorhandene Werkzeuge

- macOS auf privatem und Business-Mac; private Maschine zuerst.
- Chezmoi ist alleiniger Eigentümer globaler Agent-, MCP-, Skill-, Launcher- und Neovim-Konfiguration.
- Neovim ist bewusst schlank und viewer-first: Markdown-Rendering, Überschriftennavigation und Browser-Preview mit Mermaid sind bereits vorhanden.
- tmux-dev ist bestehende Terminal-/Pane-Infrastruktur; keine zweite konkurrierende Session- oder Worktree-Laufzeit ohne klar abgegrenzte Rolle.
- Hunk ist für lokale Diffs. GitHub mit `gh stack` ist für Pull Requests, CI und formale Reviews.
- Obsidian soll schöne Lese-, Planungs- und Verweisansicht liefern.
- Kustos/Wiki bleibt kuratierter Wissenszugang.
- Es gibt mehrere private und berufliche Wiki- bzw. Arbeitsrepos. Diese müssen als getrennte Git- und Wissensbereiche bleiben.
- Die persönliche Roadmap darf Ziele und Links enthalten, aber keine Kopien beruflicher Pläne oder Wiki-Inhalte.
- Geschäftliche Vorgaben, lokale Obsidian-Nutzung und Community-Plugins auf dem Business-Mac müssen vor Rollout geprüft werden.

## Bereits akzeptierter Kontext

Die akzeptierte Kustos-Seite **TUI Agent Environment Control Plane** empfiehlt, Agent Orchestrator (AO) zuerst als lokalen Kontroll- und Lifecycle-Layer zu testen. Agent Manager ist Rückfalloption, falls AO bei lokaler Kontrolle, Telemetrie, Konfigurationshoheit oder Recovery durchfällt.

Wichtige bisherige Leitplanken:

- Keine öffentliche Listener, Remote-Relays, Mobile-Pairing oder unreviewte Plugins.
- Kein Tool darf still in Chezmoi-verwaltete Pfade schreiben.
- Kein zweiter Live-Status in Obsidian.
- Hunk bleibt lokale Review-Oberfläche, kein Ersatz für PR-Review.
- Keine zentrale Mega-Vault und keine Kopien von Markdown zwischen Repos.

## Kernfragen

1. **Agent-Steuerung**
   - Welches konkrete Produkt erfüllt die Rolle am besten: Agent Orchestrator, Agent Manager oder andere aktuelle Alternativen?
   - Welche davon unterstützen lokale Gruppen/Workspaces, Worktrees, gemischte Codex-/Claude-Code-Worker, Follow-ups, Recovery nach Schlaf/Reboot und sauberes Cleanup?
   - Welche dokumentierten lokalen Hooks, CLI-Kommandos, APIs oder Event-Mechanismen gibt es für Gruppenwechsel bzw. Workspace-Aktivierung?
   - Gibt es Telemetrie-, Listener-, Authentifizierungs- oder Konfigurationsrisiken?

2. **Workspace-Koordinator**
   - Gibt es ein bestehendes Tool oder etabliertes Muster, das eine `workspace_id` auf Repo, Worktree, Agent-Gruppe, Obsidian-Einstieg, Neovim-Root, Hunk-Root, Issue/PR und optional Fensterlayout abbildet?
   - Falls kein passendes Tool existiert: Wie klein kann ein lokaler, ChezMoi-verwalteter Launcher oder ein Workspace-Register sein?
   - Wie lassen sich Kontextwechsel zuverlässig machen, ohne versteckte Hintergrunddienste, zweiten Statusspeicher oder fragile Bildschirm-Automatisierung?

3. **Markdown und Wissen**
   - Wie lassen sich viele getrennte Git-Wikis angenehm lesen und bearbeiten, ohne sie in eine zentrale Vault zu kopieren?
   - Welche Obsidian-Funktionen, URI-/Deep-Link-Mechanismen, Multi-Vault-/Fenster-Workflows oder sichere Ergänzungen eignen sich?
   - Welche Rolle sollten Obsidian, Neovim und ein Browser-Preview jeweils spielen?
   - Wie bleiben private und berufliche Inhalte technisch, rechtlich und organisatorisch getrennt?

4. **Review und Fenster**
   - Wie werden Hunk, Neovim und `gh stack` sauber am selben Worktree verankert?
   - Ist `yabai` für Fokus und wiederherstellbare Fensteranordnung sinnvoll, und welche Accessibility-/Security-/Business-Mac-Einschränkungen gelten?
   - Welche Erkenntnisse oder Muster aus **Omarchy** sind übertragbar? Omarchy selbst muss als Linux/Arch-orientierte Distribution bewertet werden: nicht vorschnell für macOS übernehmen, sondern prüfen, ob seine Workspace-, Launcher-, Tiling- oder Dokumentationsideen sinnvoll nachbaubar sind.

## Vergleichskandidaten und Quellen

Mindestens vergleichen:

- Agent Orchestrator und Agent Manager
- bestehendes tmux-dev als Baseline
- aktuelle, gut belegte Alternativen für lokale Agent-Orchestrierung bzw. Workspace-Management
- Obsidian-native Möglichkeiten und sichere, etablierte Ergänzungen
- Hunk- und Neovim-nahe Worktree-/Review-Flows
- yabai und mögliche macOS-Alternativen, falls relevant
- Omarchy: Funktionsumfang, Architektur, Plattformgrenzen und übertragbare Muster

Quellenhierarchie:

1. Offizielle Dokumentation, Quellcode, Release Notes und Issue Tracker
2. belastbare technische Blogs, Maintainer-Posts und Praxisberichte
3. Community-Erfahrungen nur klar als solche kennzeichnen

Aktualität, macOS-Kompatibilität, konkrete Versionen und Corporate-/MDM-Einschränkungen müssen ausdrücklich geprüft werden.

## Bewertungskriterien

| Kriterium | Muss erfüllt sein |
| --- | --- |
| Lokalität | Loopback/Unix-Socket; kein öffentlicher Dienst |
| Konfigurationshoheit | Chezmoi bleibt alleiniger Owner |
| Sicherheit | Keine Secrets in Dateien; nachvollziehbare Telemetrie und Berechtigungen |
| Worktree-Kontext | Eine Gruppe verweist eindeutig auf einen Worktree |
| Markdown-Flow | Repo bleibt Quelle; Obsidian/Neovim öffnen richtigen Einstieg |
| Review | Hunk für lokal, GitHub für PR; keine Überschneidung |
| Wiederherstellung | Verhalten nach Sleep, Reboot, Agent-Abbruch und Cleanup belegt |
| Private/Business-Trennung | Keine Vermischung von Inhalten oder privaten Konfigurationen |
| Wartbarkeit | Kleine, dokumentierte Bausteine; keine magische Automation |
| Nutzererlebnis | Wenige bewusst gestartete Schritte, schneller Kontextwechsel |

## Gewünschtes Ergebnis

Ein ausführlicher, zitierter Entscheidungsbericht mit:

1. Architekturvorschlag und klaren Verantwortungsgrenzen
2. Vergleichstabelle der Kandidaten
3. Empfehlung mit begründeter Alternative
4. konkretem `workspace_id`-Datenmodell und minimalem Workspace-Register
5. sicherem Proof-of-Concept auf privatem Mac, maximal klein und reversibel
6. Validierungs- und Recovery-Checkliste
7. dokumentiertem Business-Mac-Rollout mit Policy-Gates
8. Plan für endgültige Dokumentation: Chezmoi für Konfiguration/Runbooks, Kustos für kuratiertes Wissen, Repo-Dokumente für projektbezogene Pläne
9. Quellenverzeichnis mit Primärquellen und klar getrennten Praxisquellen

## Nicht im ersten Proof-of-Concept

- Vollautomatische bidirektionale Synchronisation zwischen Obsidian und Agent-Steuerung
- Eigener Agent-Orchestrator oder Statusdatenbank
- Ungeprüfte, globale Community-Plugins
- gleichzeitiger Betrieb konkurrierender Session-/Worktree-Runtimes
- umfangreiche yabai-Automatisierung vor bewiesenem Kernflow
