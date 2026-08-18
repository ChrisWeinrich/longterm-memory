---
title: "Gemeinsamer Wissenskern und spezialisierte Agenten-Wikis"
type: discussion
tags: [agents, architecture, long-term-memory, wiki]
state: draft
created: 2026-08-12
---

# Gemeinsamer Wissenskern und spezialisierte Agenten-Wikis

## Ausgangsfrage

Soll das Personal-Long-Term-Memory-Wiki alle Wissensbereiche zentral halten,
oder benötigen spezialisierte Assistants wie ein Health Assistant eigene
Wissensräume?

## Konsens / aktueller Stand

Dieses Repository ist als portable, kuratierte gemeinsame Gedächtnisschicht
angelegt: akzeptierte, personenübergreifend nützliche Informationen,
Entscheidungen, Forschung und Arbeitskonventionen. Der read-only Wiki-MCP
passt zu dieser Rolle als kontrollierte Ausgabeschnittstelle.

Der gemeinsame Wissenshüter heißt **Kustos**. Er ist der Generalist für
allgemeines, langlebiges und bewusst freigegebenes Wissen, nicht der
vollständige Datenspeicher jedes spezialisierten Assistants.

Ein spezialisierter Assistant kann zusätzlich einen eigenen Wissensraum
brauchen, wenn seine Notizen fachlich sensibel, sehr detailliert, kurzlebig
oder nur für seinen Zweck relevant sind. Für einen Health Assistant betrifft
das insbesondere private Gesundheitsdaten, Verlaufsdaten und fachliche
Arbeitsartefakte. Ein eigenes Wiki oder eine eigene kuratierte Sammlung kann
hier klare Verantwortlichkeiten, gezielte Zugriffsrechte und einen kleinen
Kontext ermöglichen.

Der gemeinsame Kern bleibt trotzdem sinnvoll: Er erlaubt, explizit freigegebene
und allgemein nützliche Erkenntnisse als überprüfte Informationen an andere
Assistants weiterzugeben. Das Spezial-Wiki sollte dabei nicht automatisch den
gemeinsamen Kern replizieren oder direkt verändern.

## Entscheidungen

- Der Name dieses allgemeinen Wissenshüters ist **Kustos**.

## Offene Punkte

- Welche Kategorien dürfen aus einem spezialisierten Wissensraum in den
  gemeinsamen Kern übernommen werden?
- Soll der Übergang nur über menschlich kuratierte Drafts erfolgen oder über
  eine begrenzte, getrennte Inbox?
- Welche Daten müssen ausschließlich im Health-Kontext bleiben, und welche
  technische Isolation ist dafür erforderlich?
- Reicht zunächst eine fachliche Collection im bestehenden Wiki, oder ist ein
  separates Repository mit eigenem MCP und eigenen Zugriffsrechten nötig?

## Verwandte Wiki-Seiten

- [[2026-08-12--wiki-as-shared-long-term-memory|Wiki als gemeinsames Langzeitgedächtnis]]
- [[2026-08-12--agent-trust-and-local-access-boundaries|Agent Trust and Local Access Boundaries]]
