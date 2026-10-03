---
title: "Managed Forgejo providers in Europe"
type: raw-research-report
tags: [research, forgejo, git, ci-cd, sovereignty, europe]
origin: research-workflow
created: 2026-10-01
---

# Managed Forgejo providers in Europe

## Conclusion

Neben gitbuild.dev wurden vier weitere Managed-Forgejo-Kandidaten mit
offiziellen Produkt- und Rechtsseiten gefunden. Für Christians Ziel — privater
GitHub-Ersatz mit Repos, Issues und Actions-ähnlichem CI — sind Codey.ch und
Codebahn die funktional vollständigsten Kandidaten. Codey.ch ist Schweizer
(Europa, aber nicht EU); Codebahn ist schwedisch und beansprucht EU-only
Infrastruktur. Beide benötigen vor Kauf eine kurze Vertrags- und Pilotprüfung.

## Evidence

| Anbieter | Vertragspartner / Standort | Daten und Betrieb | CI | Einordnung |
| --- | --- | --- | --- | --- |
| [Codey.ch / VSHN](https://www.forgejo.ch/) | VSHN, Zürich, Schweiz | dedizierte Instanz auf cloudscale.ch, Schweiz | Forgejo Actions enthalten | Vollständig, aber Schweiz statt EU |
| [Codebahn](https://codebahn.net/managed-forgejo-hosting/) | Hackerman AB, Göteborg, Schweden | behauptet EU-only; verschlüsselte Backups bei Hetzner Falkenstein, Runner in Paris | gehostete ephemere VM-Runner | Funktional passend; Anbieter sagt selbst, dass er noch keine SOC-2-/ISO-27001-Berichte anbietet |
| [fremforge](https://www.frem.sh/legal/terms/) | fremverk ApS, Brøndby, Dänemark | EU-souveräner Multi-Tenant-Dienst laut AGB; rechtlicher DPA/SLA-Verbund | gehostete VM je Job auf T Cloud | Funktions- und Vertragsumfang stark, aber modifizierter Forgejo-Build und junger Dienst genau prüfen |
| [By-Hoster](https://by-hoster.net/en/app-forgejo) | Anbieterangaben zur Rechtsform in diesem Schnellsuchlauf nicht ausreichend validiert | eigene Rechenzentren in Nouvelle-Aquitaine, Frankreich | nicht dokumentiert | günstiges Forgejo-Hosting, aber nicht als Actions-Ersatz belegt |
| [gitbuild.dev](https://gitbuild.dev/forgejo-hosting) | StennMedia, Breda, Niederlande | netcup Deutschland, Backups Hetzner Deutschland, DPA veröffentlicht | nicht dokumentiert | transparenter Git-/Issue-Host, CI vorher verbindlich klären |

## Trade-offs and risks

- Anbieterangaben sind offizielle Selbstauskünfte, keine unabhängige
  Zertifizierung oder Beschaffungsfreigabe.
- „Europa“ und „EU“ sind verschieden: Codey.ch hostet in der Schweiz.
- Bei CI müssen Runner-Region, Isolation, Secret-Handling, Container-Registry,
  Logs und Datenabflüsse geprüft werden; eine Forgejo-Instanz allein genügt
  nicht.
- Codebahn und fremforge legen eine deutlich umfangreichere proprietäre
  Betriebs-/Control-Plane über Forgejo. Das kann gut sein, erhöht aber gegenüber
  Standard-Forgejo die Abhängigkeit.

## Open questions

- Ist Schweiz als europäischer, aber nicht EU-Mitgliedstaat zulässig?
- Soll CI vollständig durch den Anbieter laufen oder sollen Deployments nur auf
  einem eigenen Runner im Heim-/Zielnetz erfolgen?
- Welches Mindestniveau für SLA, unabhängige Auditberichte und Support wird
  verlangt?

## Sources

Alle Quellen am 2026-10-01 abgerufen.

- [VSHN / Codey.ch: Managed Forgejo, Hosting, CI und Migration](https://www.forgejo.ch/)
- [Codebahn: Managed Forgejo, EU-Runner und Unternehmensdaten](https://codebahn.net/managed-forgejo-hosting/)
- [fremforge AGB: dänischer Vertragspartner, Service und Exit](https://www.frem.sh/legal/terms/)
- [By-Hoster: verwaltetes Forgejo, Frankreich-Hosting](https://by-hoster.net/en/app-forgejo)
- [gitbuild.dev: Managed Forgejo](https://gitbuild.dev/forgejo-hosting)
- [gitbuild.dev: Infrastruktur](https://gitbuild.dev/infrastructure)
