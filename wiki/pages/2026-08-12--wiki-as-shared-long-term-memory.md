---
title: "Wiki als gemeinsames Langzeitgedächtnis"
type: discussion
tags: [agents, mcp, long-term-memory, research, wiki]
state: accepted
created: 2026-08-12
migrated_from: wiki/sources
conversation:
  system: codex
  session_id: "019fe785-aded-7972-b916-e17cae78ca20"
  location: "/Users/christianweinrich/.codex/sessions/2026/08/09/rollout-2026-08-09T19-15-25-019fe785-aded-7972-b916-e17cae78ca20.jsonl"
  availability: local
---

# Wiki als gemeinsames Langzeitgedächtnis

## Ausgangsfrage

Wie kann ein lokales Markdown-Wiki als gemeinsames, kuratiertes
Langzeitgedächtnis für mehrere Assistant-Instanzen dienen, ohne dass Agenten
unreviewtes Wissen als Fakten verfestigen?

## Konsens / aktueller Stand

Das Wiki ist der dauerhafte, versionierte Speicher. `state: accepted` ist
kuratiertes und zitierbares Wissen; `draft` bleibt explizit unreviewed. Die
Zugriffsschicht soll ein kleiner Wiki-MCP sein, während Skills die Arbeitsabläufe
für Recherche, Diskussion und Wiki-Pflege beschreiben.

Das Wiki-Repository wurde aus `ai-assistant-template` als „Personal Long-Term
Memory“ unter `/Users/christianweinrich/Source/wiki` instanziiert. Es enthält
bereits eine lokale, read-only Wiki-MCP-Komponente sowie `research`,
`discussion` und `llm-wiki` als repo-gebundene Skills.

## Entscheidungen

- Wiki-Seiten verwenden `type`, `state` und `tags` im Frontmatter. Tags sind
  zunächst frei, kleingeschrieben und kebab-case; `wiki/sources/` bleibt
  vorerst flach.
- Forschung und Diskussion bleiben getrennte Dokumenttypen. Beide werden als
  Drafts in `wiki/sources/` abgelegt und erst nach menschlichem Review zu
  `accepted`.
- Shallow Research schreibt direkt einen Draft-Report; Deep Research verwendet
  zusätzlich die reviewten Planungsartefakte in `_research/`.
- Diskussionen werden als kurze, reviewbare Zusammenfassung gespeichert, nicht
  als kopiertes Transkript. Eine Conversation-Referenz wird nur nach Prüfung
  aufgenommen.
- Der KISS Wiki-MCP soll zunächst akzeptiertes Wissen sicher lesen:
  `wiki_discover`, `wiki_index`, `wiki_search` und `wiki_get`. `wiki_discover`
  liefert das Schema sowie tatsächlich verwendete Types und Tags.
- Externe Assistant-Instanzen sollen später einen einzigen begrenzten
  Schreibpfad erhalten: `wiki_inbox_create` erzeugt ausschließlich neue
  `state: draft`-Dateien in `inbox/`; er darf kein kuratiertes Wissen ändern.

## Offene Punkte

- Den Wiki-MCP nach lokaler Validierung für Codex, Claude und Copilot zugleich
  in der gemeinsamen, chezmoi-verwalteten Konfiguration registrieren.
- Den späteren Remote-Zugriff getrennt planen: Authentifizierung, Allowlist und
  Freigabekollektionen sind Voraussetzung; kein anonymer HTTP-MCP.
- Festlegen, welche zusätzlichen Wissensbereiche ein spezialisierter Assistant
  (etwa ein Health Assistant) später erhalten darf. Die Freigabe soll über
  explizite Kollektionen erfolgen, nicht über beliebige Ordnerzugriffe.

## Gesprächsreferenz

Die Zusammenfassung ist der reviewbare Arbeitsstand; das lokale Transkript
dient nur der Nachvollziehbarkeit:

- [Lokale Codex-Unterhaltung](file:///Users/christianweinrich/.codex/sessions/2026/08/09/rollout-2026-08-09T19-15-25-019fe785-aded-7972-b916-e17cae78ca20.jsonl)

## Verwandte Wiki-Seiten

Noch keine. Relevante Implementierungs-Handover liegen vorübergehend außerhalb
des Wiki-Repositories in `/tmp/` und sind nicht Teil des kuratierten Wissens.
