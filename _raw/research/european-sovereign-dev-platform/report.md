---
title: "Europäische souveräne Entwicklungsplattform"
type: raw-research-report
tags: [research, infrastructure, git, issues, ci-cd, roadmap, sovereignty, europe]
origin: research-workflow
created: 2026-10-01
---

# Europäische souveräne Entwicklungsplattform

## Conclusion

Für Christians Anforderung gibt es zwei sinnvolle Zielbilder:

1. **Tuleap Cloud von Enalean SAS (Frankreich)** ist der stärkste belegte
   *All-in-one*-Kandidat. Enalean ist eine französische SAS; der Vertrag
   unterliegt französischem Recht. Tuleap bietet Git, Tracker/Issues,
   Roadmap, Backlog sowie integriertes CI/CD und gibt für die Cloud Hosting in
   Frankreich an. Das ist die beste Wahl, wenn ein einziger betreuter
   europäischer Dienst wichtiger ist als Einfachheit und Preis.
2. **Forgejo selbst betreiben, auf Hetzner Cloud in Deutschland oder Finnland**
   ist die beste Wahl für maximale Souveränität und einen kleinen privaten
   Infrastruktur-Stack. Forgejo liefert Repos, Pull Requests, Issues,
   Milestones, Kanban-Boards und CI über Forgejo Actions; Hetzner ist eine
   deutsche GmbH mit Rechenzentren in Deutschland und Finnland. Du bist dabei
   selbst Betreiber, trägst aber Updates, Backups und Runner-Sicherheit.

Für die gewünschte leichte Roadmap reicht im Forgejo-Zielbild ein separates
privates Repository `infra-roadmap`: Issues als Arbeitseinheiten, Labels für
Bereich und Zeithorizont, Milestones für Quartale/Phasen, ein Kanban-Projekt
für den Ablauf. So bleiben persönliche Vorhaben und Infrastruktur-Vorhaben in
einem Backlog, ohne eine zweite Planungssoftware einzuführen. Das ist keine
portfolioübergreifende Roadmap; dafür ist **OpenProject**, ebenfalls deutsche
GmbH und selbst betreibbar, die passende spätere Ergänzung.

**Empfohlene Reihenfolge:** Erst Forgejo + ein isolierter Forgejo Runner auf
Hetzner als schlanken Pilot aufsetzen. Wenn die per-Repository-Kanban-Ansicht
für die persönliche und Infra-Roadmap nach vier bis sechs Wochen nicht reicht,
OpenProject ergänzen. Falls Managed Service von Anfang an zwingend ist und
Budget/Komplexität akzeptabel sind, stattdessen Tuleap evaluieren.

## Evidence

### Souveränitätsmaßstab

Hier bedeutet „voll europäisch“ kumulativ: europäischer Vertragspartner,
europäischer Gerichtsstand bzw. Rechtsrahmen, Verarbeitung und Speicherung in
Europa sowie kein US-kontrollierter SaaS-Anbieter. Open Source allein genügt
nicht. Selbstbetrieb stärkt die operative Souveränität, verlangt aber eigene
Verantwortung für Identität, Backups, Patchen, Secrets und CI-Runner.

| Kandidat | Europäische Firma / Vertrag | Hosting und Daten | Repos / Issues / Roadmap / CI | Einordnung |
| --- | --- | --- | --- | --- |
| **Tuleap Cloud** | Enalean SAS, Frankreich; myTuleap-Vertrag nach französischem Recht | Anbieter sagt: Cloud-Daten in Frankreich; alternativ On-Premises | Git, Tracker, Roadmap-Widget, Backlog; Anbieter beschreibt integriertes CI/CD | **All-in-one, Managed; vor Vertrag final DPA/Subprozessoren prüfen** |
| **Forgejo + Hetzner** | Forgejo wird von der Berliner Non-Profit-Organisation Codeberg e.V. getragen; Hetzner Online GmbH ist deutsch | Gewählte Hetzner-Region Deutschland oder Finnland; eigene Instanz und Datenbanken | Git, PRs, Issues, Labels, Milestones, Projects/Kanban; Forgejo Actions mit eigenem Runner | **Empfohlen: klein, souverän, aber selbst betrieben** |
| **Forgejo + OpenProject + Hetzner** | Codeberg e.V. und OpenProject GmbH (Berlin); Hetzner deutsch | Selbstbetrieb vollständig bei gewählter EU-Region | Forgejo für Code/CI, OpenProject für Work Packages, Boards, Gantt und Roadmap | Spätere Ergänzung bei echter Roadmap-/Planungsanforderung |
| **Codeberg.org** | Deutscher, gemeinnütziger Verein; Berliner Hardware | Dienste überwiegend auf eigener Hardware in Berlin | Forgejo und gehostetes CI vorhanden | **Nicht wählen:** akzeptiert keine private kommerzielle Nutzung als allgemeinen Hosting-Service; CI ist Gemeingut mit Ressourcenlimits |
| **Taiga Cloud** | Taiga Cloud Services S.L., Spanien; DPA nennt jedoch zusätzlich Kaleidos Inc. Sucursal en España als gemeinsamen Verantwortlichen | nicht ausreichend für den harten Souveränitätsmaßstab belegt | Projektplanung, kein belegter Git-/CI-All-in-one-Ersatz | **Ausschließen:** Eigentums-/Kontrolllage für „voll souverän“ nicht klar, funktional unvollständig |

### Tuleap: europäischer All-in-one-Dienst

- Enalean SAS ist nach den myTuleap-AGB in Frankreich registriert; der Vertrag
  wird in Frankreich geschlossen und französisches Recht gilt.
- Tuleap beschreibt die Cloud als durch Enalean gehostete und unterstützte
  Plattform. Seine Produktseite nennt „secure data, hosted in France or
  on-site“, integriertes Git/CI/CD und Roadmap-/Backlog-Abgleich.
- Die offizielle Dokumentation beschreibt ein Roadmap-Widget als Gantt-Ansicht
  für Tracker-Artefakte mit Zeitraum und Fortschritt. Damit kann ein
  Infrastruktur-Epic mit kleineren Tasks als echte Zeitachse dargestellt
  werden.

**Folgerung:** Tuleap erfüllt die Funktionsliste überzeugend und ist der
einfachste Weg zu einem europäischen Vertragspartner. Es ist historisch ein
ALM-Werkzeug für Teams und regulierte Umgebungen; für eine einzelne Person kann
es deutlich schwerer und voraussichtlich teurer als Forgejo sein. Preise,
Mindestvertragslaufzeit, aktuell gültiges DPA, Subprozessorliste, Backup- und
Exit-Regeln sind vor einem Kauf verbindlich anzufordern.

### Forgejo + Hetzner: maximale Kontrolle mit geringem Produktumfang

- Forgejo ist selbst hostbare freie Software; Codeberg e.V. ist ein in Berlin
  ansässiger eingetragener Verein. Forgejo dokumentiert Issues, Labels,
  Milestones und Projects/Kanban-Boards.
- Forgejo Actions ist integriertes CI. Workflows liegen unter
  `.forgejo/workflows`; die Ausführung geschieht absichtlich nicht im
  Forgejo-Server, sondern auf separaten Runnern. Ein GitHub-Actions-Workflow
  ist nicht garantiert kompatibel und benötigt in der Regel Anpassungen.
- Hetzner Online GmbH ist ein deutsches Unternehmen. Eigene Rechenzentren
  liegen laut Anbieter in Deutschland und Finnland. Der AV-Vertrag nennt die
  Hetzner Online GmbH als Anbieter.

**Sicherer Minimalbetrieb:** Forgejo und Datenbank auf einem Hetzner-Server;
Runner auf separater VM; nur private Repositories auf dem Runner; Container-
Runner statt Host-Runner; Deploy-Schlüssel und Produktionszugänge nur
zielgerichtet. Forgejo warnt ausdrücklich, dass Host-Runner keine echte
Isolation bieten und nicht zwischen nicht vertrauenswürdigen Workflows geteilt
werden sollen. Backups müssen mindestens Git-Repositories, Forgejo-Datenbank,
Anlagen, Konfiguration und Runner-Registrierung abdecken; Wiederherstellung
regelmäßig testen.

### Leichtgewichtige Roadmap ohne Tool-Sprawl

Im Repository `infra-roadmap`:

| Element | Konvention |
| --- | --- |
| Issue | eine konkrete Aufgabe, Entscheidung oder Wartungsarbeit |
| Labels | `area:network`, `area:cloud`, `area:security`, `area:home`, `type:idea`, `type:maintenance`, `priority:p1` bis `p3` |
| Milestone | ein plausibler Horizont wie `2026-Q4: Foundation`, nicht ein starres Lieferdatum |
| Projekt/Kanban | `Inbox` → `Ready` → `Doing` → `Waiting` → `Done` |
| Roadmap-Issue | ein übergeordnetes Vorhaben mit Checkboxen und Links zu Teil-Issues/Repos |

Damit entsteht ein persönlicher Inbox-/Entscheidungsort und eine operativ
nutzbare Infra-Roadmap. Erst bei mehreren parallelen Projekten, Abhängigkeiten
und Gantt-Bedarf sollte OpenProject ergänzt werden. OpenProject dokumentiert
Work Packages für Tasks, Features, Risiken, Meilensteine und Phasen, Boards,
Gantt-Charts sowie Roadmap-/Release-Planung. Es hat keine aktuelle vollwertige
Forge- oder CI-Alternative: seine Git-Integration ist zum Browsen/Verknüpfen
gedacht und für Community/On-Premises beschrieben. Deshalb ergänzt es Forgejo,
ersetzt es nicht.

## Trade-offs and risks

- **„EU-Hosting“ ist keine vollständige Souveränitätsaussage.** Jedes SaaS-
  Angebot muss im konkreten Tarif auf Unterauftragnehmer, Telemetrie,
  Supportzugriffe, E-Mail, SSO, Backups und Datenübermittlungen geprüft
  werden. Ein europäisches Unternehmen kann US-Dienste einsetzen.
- **CI ist Remote-Code-Execution.** Eine Forgejo-Instanz allein ist nicht die
  CI-Lösung; ein Runner führt fremden Code aus. Kein Runner darf mit
  unbeschränktem Zugriff auf den Host oder das ganze Heimnetz teilen.
- **Forgejo-Boards sind nicht GitHub Projects.** Sie sind gut für Kanban und
  repo-nahe Planung, aber kein flexibles, organisationsweites Portfolio-Tool.
- **Tuleap kann überdimensioniert sein.** Vor einem Pilot sind Preis,
  Bediengefühl und die tatsächlich benötigten Cloud-Module zu testen.
- **Codeberg ist kein privater Infrastruktur-SaaS.** Seine rechtliche und
  gemeinschaftliche Ausrichtung nicht mit einer bezahlten, privaten
  Unternehmensforge verwechseln.
- **Migration:** Git-Historie ist portabel. Issues, Boards, CI-Workflows,
  Secrets und GitHub-spezifische Automationen benötigen je nach Zielsystem
  gesonderte Migration bzw. Neuaufbau.

## Open questions

- Muss der Dienst rein privat sein oder gibt es eine gewerbliche/
  freiberufliche Nutzung? Das beeinflusst insbesondere Vertrag, Rechnung und
  den Ausschluss von Codeberg.
- Soll die Instanz ausschließlich per Tailscale/VPN erreichbar sein oder auch
  öffentlich für externe Kollaboration? Das bestimmt den Auth- und
  Angriffsflächenentwurf.
- Reicht ein Kanban plus Quartals-Milestones, oder werden Abhängigkeiten,
  Zeitachsen und projektübergreifende Portfolio-Sicht wirklich benötigt?
- Welche GitHub Actions werden heute genutzt? Ihre Runner-, Container- und
  Secret-Anforderungen bestimmen die Forgejo-Migration.
- Welches Budget und welcher Zeitaufwand sind für Patchen, Backups und
  Störungsbehebung akzeptabel?

## Sources

Alle Quellen am 2026-10-01 abgerufen.

- [Tuleap Produktseite: Frankreich-Hosting, Git/CI/CD, Roadmaps](https://www.tuleap.com/)
- [myTuleap Terms of Service: Enalean SAS, Frankreich und anwendbares Recht](https://www.tuleap.com/mytuleap-terms-of-service/)
- [Tuleap-Dokumentation: Roadmap-Widget](https://docs.tuleap.com/user-guide/project-admin.html)
- [Tuleap Legal Center](https://www.tuleap.com/legal/)
- [Forgejo User Guide: Issues und Milestones](https://forgejo.org/docs/v15.0/user/issue-tracking-basics/)
- [Forgejo User Guide: Projects/Kanban](https://forgejo.org/docs/latest/user/)
- [Forgejo Actions: Überblick und Runner-Modell](https://forgejo.org/docs/latest/user/actions/overview/)
- [Forgejo Actions: Sicherheitsmodell und Host-Runner-Warnung](https://forgejo.org/docs/latest/user/actions/security/)
- [Codeberg: Organisation und Berliner Sitz](https://docs.codeberg.org/getting-started/what-is-codeberg/)
- [Codeberg FAQ: Berliner Hosting und Grenzen privater kommerzieller Nutzung](https://docs.codeberg.org/getting-started/faq/)
- [Hetzner: Unternehmensbeschreibung](https://cdn.hetzner.com/assets/downloads/Umwelterklarung_Stand_30_10.pdf)
- [Hetzner: Rechenzentren Deutschland und Finnland](https://www.hetzner.com/assets/Uploads/downloads/Sicherheit-en.pdf)
- [Hetzner: Auftragsverarbeitungsvertrag](https://www.hetzner.com/AV/DPA_en.pdf)
- [OpenProject: deutscher Vertragspartner und AVV](https://www.openproject.org/de/rechtliches/nutzungsbedingungen/)
- [OpenProject: Roadmap-/Release-Planung](https://www.openproject.org/docs/user-guide/roadmap/)
- [OpenProject: Boards](https://www.openproject.org/docs/user-guide/agile-boards/)
- [OpenProject: Grenzen der Repository-Integration](https://www.openproject.org/docs/installation-and-operations/configuration/repositories/)
- [Taiga Terms: spanischer Vertragspartner](https://taiga.io/terms-and-conditions/)
- [Taiga DPA: gemeinsame Verantwortlichkeit mit Kaleidos Inc. Sucursal en España](https://taiga.io/data-processing-addendum-dpa/)
