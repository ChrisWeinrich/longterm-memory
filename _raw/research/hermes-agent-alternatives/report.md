---
title: "Hermes Agent und Alternativen — Deep-Research-Bericht"
type: raw-research-report
tags: [research, ai-assistant, agent, mcp, tailscale, obsidian]
origin: research-workflow
created: 2026-08-18
---

# Hermes Agent und Alternativen

## Conclusion

**Empfehlung: Hermes Agent als Runtime, der vorhandene Wiki-MCP als alleinige
Wissensgrenze und im MVP keine weiteren Tools.** Hermes liefert den benötigten
Kern bereits: selbst gehosteter Web-/Headless-Gateway, MCP-Client mit
Toolfilterung, getrennte Profile und Sitzungen sowie einen MCP-Servermodus.
Die offizielle CLI-Dokumentation verlangt bei nicht-lokalem Binden eine
Authentifizierung; Tailscale-only kann deshalb zusätzlich zur
Tailnet-Netzgrenze mit einer Login-Schranke betrieben werden [S1].

Keine Alternative hat für den absichtlich engen MVP einen klaren Vorteil:

- **LibreChat** ist die beste Alternative, wenn Mehrbenutzer-Web-UI und eine
  HTTP-Agenten-API wichtiger werden. Die Agenten-API ist aber ausdrücklich
  Beta [S3], und der Schnellstart bringt mehrere Dienste mit [S5].
- **Letta** ist passend, wenn stateful Agent-Memory das Produktziel ist. Hier
  wäre das eher Zusatzkomplexität, denn der Agent State lebt in einer
  Datenbank [S7], während der Markdown-Vault die kuratierte Quelle bleibt.
- **Open WebUI** kann den Wiki-MCP als Streamable-HTTP-Tool nutzen, ist aber
  primär eine Chat-/Tool-UI. Python-Tools können im Prozess beliebigen Code
  ausführen [S10]; für den MVP ist das ein zusätzlicher Kontrollbedarf.
- **Eine schlanke Eigenarchitektur** ist die Kontrollreferenz, nicht der
  Startpunkt: Das Agents SDK deckt MCP, Sessions und Tracing ab [S11], aber
  UI, Login, Status, Betrieb, Updates und Backups wären Eigenleistung.

### Minimaler Zielbetrieb

```text
Browser im Tailnet
        │ HTTPS über Tailscale, kein öffentlicher Ingress
        ▼
Hermes Dashboard / Gateway (authentifiziert, eigenes vault-Profile)
        │ nur erlaubte Read-Tools per MCP-Client
        ▼
bestehender Wiki-MCP ──► akzeptierte Markdown-Seiten im Vault

getrennt: Hermes-Sitzungen, Logs und ggf. Kurzzeit-Memory
```

Kein Filesystem-MCP, keine Shell-/Computer-Use-, Browser-, Websuche-, Schreib-
oder Infrastrukturtools. Der Wiki-MCP bleibt die Durchsetzungsgrenze; Obsidian
bearbeitet dieselben Markdown-Dateien unabhängig von der Agentenlaufzeit.

Ein späterer eigener Adapter soll nicht den Vault öffnen, sondern ausschließlich
`auftrag_starten`, `auftrag_status` und `ergebnis_lesen` liefern. Ohne echten
asynchronen Bedarf wird er nicht gebaut.

## Evidence

### Vergleichsmatrix

| Kriterium | Hermes Agent | LibreChat | Letta | Open WebUI | Schlanke Eigenarchitektur |
| --- | --- | --- | --- | --- | --- |
| Betriebsrolle | Agent-Runtime mit Gateway/Dashboard | Self-hosted Web-App mit Agents | Stateful Agent Runtime + ADE/API | Web-Chat-/Tool-UI | selbst zu implementieren |
| Wiki-MCP als Client | Ja; Server hinzufügen, testen, Tools konfigurieren [S1] | Ja; Agent Builder, einzelne Tools [S4] | Ja; stdio, SSE, Streamable HTTP [S8] | Ja; Streamable HTTP, admin-gesteuert [S9] | Ja; stdio und Streamable HTTP [S12] |
| MCP-Server für andere Clients | Ja; `hermes mcp serve`, Conversation-/Message-Werkzeuge [S1] | nicht in geprüften Quellen belegt | nicht in geprüften Quellen belegt | nicht in geprüften Quellen belegt | separat zu bauen |
| API / Sitzungen / Status | Sessions; Headless JSON-RPC/WebSocket [S1] | Chat Completions/Open Responses, Beta [S3] | persistierter Agent State, ADE [S6][S7] | OpenAI-kompatibles Chat-API [S13] | Sessions/Traces, Statusmodell selbst [S11][S12] |
| Berechtigungen | Nicht-lokal: Passwort oder OAuth; Toolauswahl [S1] | API Keys, ACLs und Feature-Flags [S3][S4] | API-key-/Servermodell; Self-hosted Auth hier nicht abschließend verifiziert | MCP nur Admins; Access Control [S9] | vollständig eigene Verantwortung |
| Speichertrennung | Profile haben separate Home-, Config-, Session-, Skill-Zustände [S1] | zusätzlicher Chat-/Agentenzustand | Datenbank-Agent-State zentral [S7] | Chat-/Tool-Konfiguration separat | frei definierbar |
| Update / Backup | `update --check`, Vor-Update-Backups, Profile exportierbar [S1] | Deployment- und Datenbankbetrieb | Datenbank- und Agent-State-Backup | Container-/Anwendungsdaten | vollständig eigene Verantwortung |

### Hermes Agent

`hermes dashboard` ist eine Web-UI für Konfiguration, Schlüssel und
Sitzungsüberwachung; `hermes serve` ist das headless JSON-RPC/WebSocket-
Backend. Das Dashboard bindet standardmäßig an `127.0.0.1`. Bei nicht-lokalem
Bind verlangt die Dokumentation einen Passwort- oder OAuth-Anbieter [S1].
Das stützt Tailscale-Bindung plus Anwendungsauthentifizierung.

Hermes kann MCP-Server per Command oder URL hinzufügen, testen und die
Toolauswahl konfigurieren [S1]. Die MCP-Anleitung dokumentiert `include` und
`exclude` für Server-Tools [S2]. Für den Wiki-MCP werden daher ausschließlich
lesende Such- und Abrufwerkzeuge freigegeben, nie ein Filesystem-Server.

`hermes mcp serve` ist vorhanden, aber die dokumentierte Oberfläche betrifft
Conversations und Messages statt eines allgemeinen Job-API [S1]. Ein eigener
enger Auftragsadapter ist für spätere Statusabfragen sauberer. Profile sind
isolierte Instanzen mit eigenem Home, Config, Sessions und Skills und können
exportiert/importiert werden [S1]. Ein dediziertes `vault`-Profile trennt den
MVP vom übrigen Agentenbetrieb.

### LibreChat

LibreChat ist eine selbst gehostete Webanwendung. Der Docker-Schnellstart
startet LibreChat mit MongoDB, MeiliSearch und RAG API [S5]. MCP-Server lassen
sich konfigurieren und für Agents bis auf einzelne Tools beschränken; ACLs und
Feature-Flags kontrollieren Server-/Benutzerrechte [S4]. Die Agents API bietet
OpenAI-kompatible Chat Completions und Open Responses mit API-Key, ist aber
explizit Beta [S3]. Damit ist LibreChat ein guter späterer API-first Ersatz,
nicht der klar bessere MVP.

### Letta

Letta bietet App Server/SDK und die ADE zum Testen und Überwachen stateful
Agents [S6]. Der AgentState wird im Datenbank-Backend persistiert; Core-,
Archival- und Recall-Memory gehören zum Modell [S7]. Letta kann MCP per stdio
(nur self-hosted), SSE oder Streamable HTTP anbinden [S8].

**Inference:** Der Wiki-MCP könnte die Wissensgrenze auch hier bewahren. Für
den MVP ist Letta trotzdem überdimensioniert, weil seine eigene Memory-Welt
die Verwechslung von Laufzeitdaten mit reviewpflichtigem Markdown wahrschein-
licher macht. Nur wählen, wenn editierbarer, dauerhafter Agent-State selbst
zum Produktziel wird.

### Open WebUI

Open WebUI unterstützt MCP ab v0.6.31 nativ über Streamable HTTP. Nur Admins
legen MCP-Server an; diese lassen sich via Access Control an Nutzer oder
Gruppen vergeben [S9]. Der vorhandene Wiki-MCP ist stdio. Für Open WebUI wäre
somit ein kleiner Streamable-HTTP-Wrapper oder Proxy nötig, während Hermes und
Letta stdio können. Tools/Functions/Pipes/Filters/Pipelines führen beliebigen
Python-Code auf dem Server aus [S10] und bleiben daher im MVP deaktiviert.

### Schlanke Eigenarchitektur

Das OpenAI Agents SDK bietet Agent Loop, MCP-Toolserver, Sessions, Guardrails
und Tracing [S11][S12]. Sessions können gegen einen eigenen Speicher-Backend
implementiert werden [S12].

**Inference:** Eine Eigenarchitektur kann die kleinste Angriffsfläche ergeben,
weil sie nur den Wiki-MCP, eine authentifizierte Route und eine kleine
Job-Tabelle braucht. Sie ist dennoch nicht die Startempfehlung, weil UI,
Login, Deployment, Audit, Status, Updates und Backups neu gebaut und gewartet
werden müssten.

## Trade-offs and risks

- **Modell-Datenfluss:** Mit externem Modellanbieter verlässt Promptinhalt den
  Host. Der MVP verwendet deshalb ein explizites Modellprofil und gibt weder
  Rohdateien noch Secrets als Toolresultate aus.
- **Tailscale allein genügt nicht:** Tailnet-Zugang ersetzt keine Runtime-
  Anmeldung oder Tool-Berechtigung. Für Hermes ist die Auth-Pflicht beim
  nicht-lokalen Bind belegt [S1]. Ziel: Geräte-/Tailnet-Policy plus Password
  oder OIDC.
- **MCP ist nicht automatisch sicher:** Tooloberflächen einzeln minimieren und
  neue MCP-Server wie Code prüfen. Open WebUI beschreibt die Macht und das
  Risiko von MCP ausdrücklich [S9]; Hermes und LibreChat erlauben Granularität
  [S2][S4].
- **Memory-Verwechslung:** Sessions und Logs sind Laufzeitdaten. Nur manuell
  kuratierte Markdown-Seiten werden Wissen. Keine Runtime darf direkt in
  `wiki/pages/` schreiben.
- **Versionsdrift:** Alle Aussagen gelten zum Abrufdatum 2026-08-18. Vor dem
  Rollout Version, Bind-Adresse, Auth, MCP-Tools und Backups erneut prüfen.

## Migration path from the current template

1. Wiki-MCP unverändert als read-only stdio-Server nutzen und nur
   `wiki_discover`, `wiki_index`, `wiki_search` und `wiki_get` freigeben.
2. Frisches Hermes-Profile `vault` erstellen; keine bestehenden Skills,
   Memory-Provider oder MCPs klonen. Profilzustand separat sichern.
3. Gateway ausschließlich im Tailnet bereitstellen und Anwendungsauth für
   nicht-lokales Binden konfigurieren. Kein öffentlicher Reverse Proxy/Funnel.
4. Modellzugang als Secret außerhalb des Vaults ablegen; keine Dateipfade in
   Prompts, keine Schreib-/Exec-Tools aktivieren.
5. Abnahme testen: Tailnet-only; keine freie Datei-Leseoperation; Wiki-Abfrage
   per MCP; Obsidian bearbeitet die Dateien weiter; ein externer oder
   Infrastrukturauftrag wird abgelehnt statt ausgeführt.
6. Erst bei tatsächlichem asynchronem Bedarf den separaten authentifizierten
   Drei-Tool-Adapter ergänzen. Er speichert Auftragmetadaten/Ergebnisse, nie
   Vaultinhalt, und exportiert keine Exec-Tools.

## Open questions

- Welche Hermes-Version und welche Authentifizierung (Passwort oder eigenes
  OIDC) soll der Rollout verwenden?
- Wer im Tailnet darf den Agenten erreichen? Das bestimmt ACL und Loginumfang.
- Welcher Modellanbieter oder welches lokale Modell ist für die Datenklasse
  akzeptabel?
- Reicht synchroner Chat im MVP, oder besteht wirklich Bedarf für den
  Auftragsadapter?
- Vor einem späteren LibreChat-Wechsel: Ist dessen Agenten-API dann stabil?

## Sources

Alle Quellen sind Primärdokumentation; abgerufen am 2026-08-18. Ohne
verfügbares Veröffentlichungsdatum ist das Abrufdatum angegeben.

- **[S1] Hermes Agent, CLI Commands Reference.** https://hermes-agent.nousresearch.com/docs/reference/cli-commands
- **[S2] Hermes Agent, Use MCP with Hermes.** https://github.com/hermes-agent-org/hermes/blob/main/website/docs/guides/use-mcp-with-hermes.md
- **[S3] LibreChat, Agents API (Beta).** https://www.librechat.ai/docs/features/agents_api
- **[S4] LibreChat, MCP.** https://www.librechat.ai/en/docs/features/mcp
- **[S5] LibreChat, Quick Start.** https://www.librechat.ai/docs/quick_start
- **[S6] Letta, Agent Development Environment.** https://docs.letta.com/agent-development-environment/ade/
- **[S7] Letta, Agents API reference.** https://docs.letta.com/api/resources/agents
- **[S8] Letta, Create MCP server API reference.** https://docs.letta.com/api/typescript/resources/mcp_servers/methods/create/
- **[S9] Open WebUI, Model Context Protocol.** https://docs.openwebui.com/features/extensibility/mcp/
- **[S10] Open WebUI, Tools & Functions.** https://docs.openwebui.com/features/extensibility/plugin/
- **[S11] OpenAI Agents SDK (TypeScript), Overview.** https://openai.github.io/openai-agents-js/
- **[S12] OpenAI Agents SDK (TypeScript), MCP and Sessions.** https://openai.github.io/openai-agents-js/guides/mcp/ ; https://openai.github.io/openai-agents-js/guides/sessions/
- **[S13] Open WebUI, API Endpoints.** https://docs.openwebui.com/reference/api-endpoints/
