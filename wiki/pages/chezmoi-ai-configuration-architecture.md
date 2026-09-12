---
title: "ChezMoi AI-Konfigurationsarchitektur"
type: discussion
tags: [chezmoi, ai-configuration, mcp, skills, architecture]
state: draft
created: 2026-09-12
sources:
  - "_raw/conversations/2026-08-18--chezmoi-ai-structure-review.md"
---

# ChezMoi AI-Konfigurationsarchitektur

## Initial question

Wie lassen sich die verteilten AI-Konfigurationen im ChezMoi-Repository
verständlich als zusammenhängendes System orientieren und warten?

## Consensus / current state

ChezMoi ist die Quelle der Wahrheit. Gemeinsame Templates bestimmen MCPs,
Instructions und Berechtigungen; Agentenadapter für Codex, Claude und Copilot
setzen sie aus. Merge-Templates erhalten laufzeitverwalteten Zustand, und
Apply-Hooks synchronisieren Skills, Integrationen und den Abbau alter
Definitionen.

Die technische Struktur ist kohärent, aber schwer auffindbar, weil sie sich an
ChezMoi-Zielpfaden statt an einem AI-Einstiegspunkt orientiert.

## Open questions

- Soll es eine kurze, domänenorientierte AI-Architekturkarte mit Quell-, Ziel-
  und `chezmoi apply`-Lebenszyklus geben?
- Sollen die Listen zur Bereinigung alter MCPs zentralisiert oder ihre
  absichtlichen Adapterunterschiede dokumentiert werden?
- Soll die dokumentierte und tatsächliche Business-Behandlung des Claude-
  Skill-Sync-Hooks angeglichen werden?

## Related Wiki pages

- [[kustos-agent-runtime-and-research-boundary]]
