---
title: "Codebahn als europäische Forgejo- und Agentenplattform"
type: raw-research-report
tags: [research, codebahn, forgejo, ci-cd, mcp, cli, coding-agents, sovereignty]
origin: research-workflow
created: 2026-10-01
---

# Codebahn als europäische Forgejo- und Agentenplattform

## Conclusion

Codebahn ist ein technisch ungewöhnlich vollständiger Managed-Forgejo-Kandidat:
Repos, private Issues/PRs, Forgejo Actions auf in Paris betriebenen Runnern,
Container-Registry, CLI und ein HTTP-MCP-Server sind dokumentiert. Der
Vertragspartner ist die schwedische Hackerman AB; Primärbetrieb erfolgt bei
Scaleway in Frankreich, Backups bei Hetzner in Deutschland. Die veröffentlichten
Unterauftragnehmer sind EU-Unternehmen.

**Die wichtige Grenze:** Codebahn ist kein gehosteter Coding-Agent-Runtime.
Die Doku beschreibt MCP und CLI als Steueroberfläche für einen extern laufenden
Agenten (z. B. Codex oder Claude Code). Ein solcher Agent erhält nach OAuth
die Rechte des angemeldeten Codebahn-Nutzers und kann darunter auch Issues,
PRs und CI ändern bzw. starten. Der Agent selbst, sein Modellanbieter und seine
lokalen Datenflüsse sind nicht Teil der Codebahn-Souveränitätszusage.

Ein Pilot ist sinnvoll, aber nur mit klaren Grenzen: ein unkritisches privates
Testrepo, keine Produktionssecrets, ein separater Codebahn-Benutzer bzw. eine
eng berechtigte Organisation und zunächst nur lesendes MCP. Erst nach Test von
Export, CI, Berechtigungen und externer Egress-Analyse sollten echte
Infrastruktur-Repos folgen.

## Evidence

### Betreiber, Vertrag und Datenpfad

- Codebahn wird laut eigener Souveränitätsdokumentation von **Hackerman AB**
  (Org.-Nr. 559079-1918) in Göteborg, Schweden betrieben; schwedisches Recht
  gilt für Verträge und der DPA folgt der DSGVO.
- Die Codebahn-Privacy-Policy nennt Primärinfrastruktur bei **Scaleway** in
  Paris (`fr-par`) und Backups bei **Hetzner** in Falkenstein (`fsn1`). Das
  veröffentlichte DORA-Register nennt außerdem Mollie (NL, Zahlung) und Crisp
  (FR, Supportchat), nicht im Repository-/CI-Datenpfad.
- Die AGB-/DPA- und Infrastrukturinformationen sind öffentlich. Nach der
  Privacy-Policy soll Customer Data die EU/den EWR nicht verlassen; diese
  Aussage ist eine Anbieterzusage, kein unabhängiger Auditnachweis.
- Eine unabhängige Prüfung bestätigt, dass Hackerman AB als aktives schwedisches
  Unternehmen besteht. Sie zeigt zugleich den zentralen Betriebsrisikofaktor:
  2025 war nur eine Person beschäftigt. Die eigene Continuity-Seite bestätigt,
  dass Codebahn von einer Person betrieben wird und eine zweite Engineering-
  Kapazität erst im Aufbau ist.
- Codebahn erklärt selbst, keine ISO-27001- oder SOC-2-Type-II-Zertifizierung
  zu besitzen. Damit ist es für einen kleinen privaten Stack plausibel, für
  auditpflichtige/entscheidende Systeme aber derzeit kein passender Anbieter.

### Forgejo, Issues und Exit

- Codebahn basiert auf Forgejo und dokumentiert, dass Standard-Forgejo-API,
  Git, SSH, Branch Protection und Actions-Syntax gelten, während eigene
  Erweiterungen separat dokumentiert sind.
- Der Organisations-Export enthält Git-Historie, Issues, PRs, Kommentare,
  Labels, Milestones, Releases und Reviews als Standard-Git plus YAML; die
  Metadaten lassen sich mit Forgejos `restore-repo` wieder einspielen. Teams,
  Berechtigungen, CI-Historie/-Logs, Caches, Tokens und Secrets migrieren nicht
  automatisch.
- Die Exit-Seite verspricht kostenlosen Self-Service-Export, mindestens 30 Tage
  Abrufbarkeit nach Ende und Löschung der Customer Data innerhalb von 90 Tagen
  nach dem Retrieval-Fenster. Das senkt, aber beseitigt nicht, das
  Ein-Personen-Anbieter-Risiko.

### CI/CD und tatsächliche Souveränitätsgrenzen

- Gehostete Jobs laufen laut Runner-Doku auf Scaleway in Paris. Jeder Job läuft
  in einer isolierten, ephemeren VM; Jobs desselben Tenants teilen keinen
  Zustand. Innerhalb der VM laufen Docker-Container. Der Metadata-Endpunkt ist
  blockiert, sonst ist ausgehender HTTPS- und DNS-Verkehr erlaubt.
- `ubuntu-latest` ist ein Alias für Codebahn-Runners. Der Dienst verwendet
  Forgejo-Actions-Syntax und liest auch `.github/workflows/`; Linux ist die
  einzige gehostete Runner-Plattform. GitHub-spezifische Funktionen wie
  CodeQL, Pages und OIDC-Federation funktionieren nicht.
- Eigene Runner können parallel per eigenem Label angebunden werden. Das ist
  der passende Weg für Deployments, die Zugriff auf ein Heimnetz/Tailnet oder
  private Zielsysteme benötigen; ein solcher Runner muss separat isoliert und
  betrieben werden.
- Die häufigsten Actions können mit einer Codebahn-URL von lokalen Mirrors
  bezogen werden. **Aber:** Die Spiegel werden laut Doku täglich von GitHub
  synchronisiert; weitere Actions lösen standardmäßig direkt von GitHub auf.
  Für eine harte „kein US-Dienst in der Lieferkette“-Regel müssen Workflows
  vollständig auf lokale Actions, selbst verwaltete Actions und EU-Registries
  beschränkt werden. Auch Paketregistries, Container-Images und externe
  Deploymentziele können Daten/Metadaten außerhalb der EU verarbeiten.
- Die Dokumentation ist beim aktuellen CI-Einschluss widersprüchlich: die
  Startseite nennt 200 Solo-Minuten, eine CI-Anleitung sagt hingegen, gehostete
  Runner seien nur im Crew-Plan enthalten. Vor einem Kauf muss dies schriftlich
  geklärt werden.

### CLI und REST API

- Die Open-Source-CLI `codebahn` ist für Linux/macOS (neu auch Windows) als
  Binary verfügbar und kann auch aus dem Quellcode gebaut werden. Sie nutzt
  Browser-OAuth; Refresh-Tokens liegen in
  `~/.config/codebahn/config.json` (respektiert `XDG_CONFIG_HOME`). Für
  Headless-Abläufe ist ein Personal Access Token vorgesehen.
- Die CLI kann Repositories, Dateien, Branches, Issues, PRs, CI-Runs,
  Suche sowie Import/Mirroring bedienen und liefert mit `--json` maschinenlesbare
  Ausgabe. Damit ist sie für Skripte und lokale Agenten praktikabel.
- Codebahn stellt die REST API unter `https://codebahn.net/api/v1` bereit.
  Sie unterstützt Tokens oder OAuth/PKCE. CORS ist absichtlich für alle Origins
  geöffnet; Browser senden dabei keine Cookies, aber ein bewusst übergebener
  Token autorisiert den Zugriff. Tokens gehören daher nie in getrackte
  `.mcp.json`- oder Konfigurationsdateien.

### MCP und Coding Agents

- Der MCP-Endpunkt ist `https://codebahn.net/mcp`. Die Dokumentation nennt
  direkte Konfigurationen für Codex, Claude Code, VS Code/Copilot und Cursor.
  OAuth wird im Browser bestätigt; Zugriffsrechte werden über die normale
  Codebahn-API geprüft und auditierbar geloggt.
- Der Server bietet nach Anbieterangabe 54 Tools: Repos/Dateien/Branches,
  Issues, PRs mit Reviews und Merge, Suche sowie CI starten/Logs lesen/
  abbrechen. Der MCP-Server ist technisch ein Adapter über die Codebahn-
  REST-API und besitzt keine unabhängige Berechtigungsgrenze.
- Der angemeldete Account verleiht dem Agenten Lese- und Schreibrechte auf
  alles, was dieser Account erreichen kann. OAuth-Tokens haben laut Doku
  vollen Zugriff. Daher ist für Coding Agents ein separates Konto/Team mit
  minimalen Repo-Rechten sinnvoll; keine Org-Owner- oder Produktionssecrets in
  der ersten Integration.
- **Keine eigene Agent-Laufzeit belegt:** Die offizielle Dokumentationsstruktur
  und die Agentenseiten beschreiben ausschließlich externe Clients, MCP und
  CLI; es gibt keine dokumentierte Ausführung eines LLM, Agent-Queue,
  Agent-Sandbox oder Modellanbieter durch Codebahn. Das ist eine begründete
  Negativfeststellung aus der öffentlichen Dokumentation, keine Garantie über
  unveröffentlichte Funktionen.
- Ein Agent kann CI über MCP auslösen, aber CI ist keine sichere Agentensandbox:
  ein Workflow führt beliebigen Code aus und dessen Secrets/Netzrechte müssen
  unabhängig beschränkt werden. Einen LLM-Agenten in CI mit API-Schlüssel zu
  betreiben würde zusätzliche externe Modell-Datenflüsse einführen und ist
  nicht Teil dieser Empfehlung.

### Empfohlener Pilot

1. Vertrag, DPA, aktuelle Subprozessorliste und tatsächlichen Solo-/Crew-
   CI-Umfang vor Kontoeröffnung sichern.
2. Ein unkritisches Testrepo importieren; Export durchführen und auf einer
   lokalen Forgejo-Testinstanz mit `restore-repo` testen.
3. Ein Build ohne Secrets auf gehostetem Runner ausführen. Danach prüfen, ob
   jedes `uses:`, Image und Paketdownload innerhalb der akzeptierten
   Lieferkette liegt.
4. Einen separaten, nur auf das Testrepo berechtigten Agenten-Benutzer via MCP
   verbinden. Zuerst nur Repo lesen, Issue erstellen und CI-Log lesen; kein
   Merge und kein CI-Dispatch.
5. Erst dann einen eigenen, streng isolierten Runner für Deployments testen.
   Dieser erhält ausschließlich die Zielnetz- und Secret-Berechtigungen, die
   ein einzelner Deploy-Workflow benötigt.
6. Nach vier Wochen bewerten: Verfügbarkeit, Support, Exporttest,
   Workflow-Kompatibilität, Egress, Agentenrechte und Ein-Personen-Risiko.

## Trade-offs and risks

- Der EU-Firmen- und Datenpfad ist gut dokumentiert, doch die Beleglage beruht
  überwiegend auf Selbstauskünften; es gibt keine ISO-/SOC-Auditberichte.
- Das Haupt-Geschäftsrisiko ist nicht Forgejo, sondern ein kleiner,
  personenabhängiger Managed-Service-Betreiber. Lokale Git-Mirror/regelmäßige
  Exporte sind deshalb Pflicht.
- Codebahns MCP ist sehr mächtig. Er reduziert Integrationserzeugung, aber
  erhöht die Folgen eines fehlgeleiteten Agents oder kompromittierten Clients.
- „GitHub-Actions-kompatibel“ bedeutet nicht vollständig GitHub-kompatibel:
  Windows/macOS, CodeQL, Pages, OIDC und GitHub-API-gebundene Actions fallen
  aus oder müssen ersetzt werden.
- Externe PaaS-Anbindungen in der Environments-Doku (u. a. Vercel, Netlify,
  Render, Railway und Cloudflare Pages) sind nicht mit einem harten
  EU-only-Ziel vereinbar, sofern deren Vertrags-/Datenlage nicht separat
  geprüft ist.

## Open questions

- Gilt der aktuelle Solo-Plan tatsächlich mit 200 gehosteten CI-Minuten oder
  ausschließlich als BYO-Runner-Plan?
- Welche EU-Container-Registry, Paketquellen und Actions sollen verbindlich
  zugelassen werden, damit CI nicht stillschweigend GitHub/Docker Hub oder
  andere Drittstaatdienste nutzt?
- Reicht der veröffentlichte 48-Stunden-Incident-Notice für Christians
  Einsatzfall?
- Kann Codebahn für die beabsichtigte Nutzung ein aktuelles DPA/AVV,
  Unterauftragnehmer-Anhang und Support-/Kontinuitätszusage individuell
  bestätigen?
- Soll ein externer Coding Agent nur Issues/PRs vorbereiten oder auch mergen
  und Deploy-Workflows starten? Diese Entscheidung bestimmt das MCP-
  Berechtigungsmodell.

## Sources

Alle Quellen am 2026-10-01 abgerufen.

- [Codebahn: Souveränität, Vertragspartner und Datenpfad](https://codebahn.net/docs/sovereignty/)
- [Codebahn: Privacy Policy und Datenstandorte](https://codebahn.net/privacy/)
- [Codebahn: DORA-Register und Unterauftragnehmer](https://codebahn.net/dora/)
- [Codebahn: Security und fehlende Zertifizierungen](https://codebahn.net/security/)
- [Codebahn: Continuity und Ein-Personen-Betrieb](https://codebahn.net/continuity/)
- [Schwedisches Firmenregister-Kontext: Hackerman AB](https://www.bolagsfakta.se/5590791918-Hackerman_AB)
- [Codebahn: CI Runner, Isolation, Kompatibilität und BYO](https://codebahn.net/docs/ci-runners/)
- [Codebahn: lokale Action Mirrors](https://codebahn.net/docs/action-mirrors/)
- [Codebahn: CLI](https://codebahn.net/docs/cli/)
- [Codebahn: MCP Server](https://codebahn.net/docs/guides/mcp/)
- [Codebahn: AI-assistant integration and tool scope](https://codebahn.net/docs/guides/mcp-ai-assistants/)
- [Codebahn: Datenexport](https://codebahn.net/docs/export/)
- [Codebahn: Exit-Verfahren](https://codebahn.net/leaving/)
- [Codebahn: GitHub-Migration und Einschränkungen](https://codebahn.net/docs/guides/migrate-from-github/)
- [Forgejo Actions: Sicherheitsmodell](https://forgejo.org/docs/latest/user/actions/security/)
