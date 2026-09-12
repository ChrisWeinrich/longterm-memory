---
title: "Persönliches Finanz- und Marktdaten-Dashboard"
type: research-report
tags: [research, finance, market-data, dashboard, self-hosting]
state: draft
created: 2026-08-21
sources:
  - "_raw/research/personal-finance-market-dashboard/report.md"
  - "_raw/research/personal-finance-market-foundations/report.md"
---

# Persönliches Finanz- und Marktdaten-Dashboard

## Conclusion

Die beste erste Lösung ist **Portfolio Performance plus Koyfin Free**:

- Portfolio Performance führt die eigenen Transaktionen, Bestände, Gebühren,
  Ausschüttungen und Performance lokal und nachvollziehbar.
- Koyfin dient als getrenntes Markt-Cockpit für Aktienmärkte, globale
  Staatsanleiherenditen, Zinskurven und Makrodaten.
- TradingView ist eine optionale Ergänzung, wenn Charts und Alerts wichtiger
  sind als ein geordneter Makroüberblick.

Ein vollständiger Eigenbau ist zunächst nicht sinnvoll. Die eigentliche
Schwierigkeit sind korrekte Cashflows, Kapitalmaßnahmen, Fremdwährungen,
Instrumentzuordnung und Datenrechte, nicht die Darstellung von Charts.

Wenn nach vier Wochen ein integriertes, lokales Dashboard weiterhin einen
klaren Mehrwert bietet, ist **Wealthfolio plus ein eigenes, nur lesendes
`market-cockpit`-Add-on** der aussichtsreichste Pilot. Das Add-on sollte
offizielle Zins- und Makroquellen direkt verwenden. Portfolio Performance
bleibt so lange die Referenz für Performance und Bestände, bis beide Systeme
reconciled sind.

Parqet ist die komfortable Cloud-Alternative, wenn automatische Importe
deutscher Broker wichtiger sind als vollständige lokale Datenhaltung.

## Evidence

### Das Zielbild

Das Dashboard sollte vier Fragen in wenigen Sekunden beantworten:

1. Wie hoch sind Vermögen, Cash und heutige beziehungsweise langfristige
   Veränderung?
2. Welche Positionen, Assetklassen, Regionen und Währungen treiben Rendite und
   Risiko?
3. In welchem Aktien-, Zins- und Kreditmarktregime befinden wir uns?
4. Von wann und aus welcher Quelle stammt jeder angezeigte Wert?

Ein zweckmäßiges Layout besteht aus:

- Portfolio-Kopfzeile: NAV, Tagesänderung, YTD, TTWROR, Drawdown und Cash;
- Holdings und Risiko: Beiträge, Allokation, Konzentration und FX-Exposition;
- Aktienmärkte: Welt, USA, Europa, Deutschland, Emerging Markets und Japan;
- Zinsen und Bonds: EZB/Fed, Bund- und US-Treasury-Kurve, 2s10s, Realzins und
  gegebenenfalls Credit Spreads;
- FX, Rohstoffe und wenige Makroindikatoren;
- sichtbarer Datenqualität: Quelle, Stand, Verzögerung, fehlende Kurse und
  letzter erfolgreicher Import.

Realtime, Newsfeeds, Kursziele, technische Signale und Prognosen gehören nicht
in Version 1. End-of-day-Daten reichen für langfristige Portfolio- und
Regimebeobachtung und reduzieren Kosten und Lizenzkomplexität erheblich.

### Bondmarkt korrekt darstellen

„Bond Market“ ist nicht ein einzelner Wert. Die Anzeige muss unterscheiden:

- **Staatsanleihe-Zinskurven:** Renditen für 2, 5, 10 und 30 Jahre;
- **Kurvenform:** etwa 10 Jahre minus 2 Jahre;
- **Kreditrisiko:** Investment-Grade- und High-Yield-Spreads;
- **gehaltene Bonds:** Preis, Nennwert, Kupon, Fälligkeit, Duration und YTM;
- **Bond-ETFs:** Marktpreis beziehungsweise NAV eines Fonds, nicht die
  Staatsrendite.

Offizielle Staatsrenditen sind kostenfrei verfügbar. Ein umfassender,
kostenloser und rechtlich stabiler Feed für einzelne Unternehmensanleihen ist
dagegen nicht realistisch; hier sind Brokerdaten oder ein bezahlter Anbieter
nötig.

### Produktvergleich

| Produkt | Stärke | Grenze | Rolle |
| --- | --- | --- | --- |
| Portfolio Performance | lokale Depotbuchhaltung, deutsche PDF-/CSV-Importe, TTWROR/IRR und Risiko | kein umfassendes Markt-/Makroterminal | führendes Portfolio-Buch |
| Parqet | sehr bequeme deutsche Brokerimporte und Weboberfläche | Cloud und kein vollständiges Bondterminal | Komfortalternative |
| Wealthfolio | lokale SQLite-Daten, modernes UI, Add-on-System | jünger, weniger deutsche Brokerautomatik | integrierter Pilot |
| Koyfin | Markt-, Makro-, Bond- und Zinskurven-Dashboards | keine deutsche Transaktionsbuchhaltung; Cloud | sofortiges Markt-Cockpit |
| TradingView | breite Marktabdeckung, Charts und Alerts | Portfolioanalyse und Makroordnung schwächer | optionale Ergänzung |
| Ghostfolio | selbst gehosteter Web-Tracker | PostgreSQL/Redis und größerer Betriebsaufwand | für den Single-User-Fall unnötig schwer |
| OpenBB | viele standardisierte Datenprovider | kein persönliches Portfolio-Buch | möglicher Eigenbau-Adapter |

Portfolio Performance speichert lokal, importiert laut Dokumentation PDFs von
mehr als 90 Banken und Brokern und bietet etablierte Performance- und
Risikokennzahlen. Koyfin dokumentiert globale Staatsrenditen für 45 Länder und
Zinskurven für 20 Länder; der freie Tarif reicht für einen begrenzten ersten
Marktschirm. Wealthfolio verwendet lokal SQLite und erlaubt eigene
TypeScript-/React-Seiten mit expliziten Berechtigungen für Portfolio,
Performance, Marktdaten, Netzwerk und Secrets.

### Datenquellen für einen späteren Eigenbau

| Bereich | Bevorzugte Quelle | Wichtige Grenze |
| --- | --- | --- |
| Eigene Transaktionen | Broker-PDF/CSV über Portfolio Performance oder Parqet | Endbestand, Stückzahl und Cash abgleichen |
| EZB-Sätze und EUR-FX | ECB Data Portal API | Serienmetadaten und Aktualität speichern |
| Deutsche Bund-Kurve | Bundesbank SDMX | Kurvenmethode und Laufzeit korrekt benennen |
| Bundeswertpapiere | Bundesbank nach ISIN | kein Corporate-Bond-Universum |
| US-Treasury-Kurve | US Treasury CSV/XML | Par Yield ist kein Bondpreis |
| EU-Makro | Eurostat API | Revisionen beziehungsweise fehlende historische Vintages |
| US-/globales Makro | FRED API | Key, Attribution und Serienrechte |
| Instrument-Mapping | ISIN + MIC, optional OpenFIGI | Ticker allein ist nicht eindeutig |
| Globale Aktien/ETFs | bestehender Trackerfeed oder optional EODHD EOD | häufig indikativ, nicht börsenoffiziell |
| Offizielle Indexlevels | lizenzierter Terminal- oder Indexanbieter | Lizenzkosten und Weitergaberechte |

Für ein privates Dashboard sind liquide ETF-Proxys oft praktischer als
offizielle Indexlevels: Sie sind investierbar, als End-of-day-Kurs leichter zu
beziehen und bilden häufig Total Return besser ab. Proxy, Handelsplatz,
Währung und Abweichung zum eigentlichen Index müssen sichtbar gekennzeichnet
werden. Exakte Indexanzeigen können in Koyfin oder TradingView verbleiben,
anstatt deren Werte in den eigenen Stack zu kopieren.

### Empfohlene Reifegrade

**A — sofort, kostenlos:** Portfolio Performance und Koyfin Free einrichten,
einen repräsentativen Broker importieren, Bestände und Cash abgleichen und vier
Wochen lang echte Informationslücken notieren.

**B — lokaler Integrationspilot:** Wealthfolio lokal parallel betreiben und
ein kleines Read-only-Add-on für ECB, Bundesbank und US Treasury bauen. Jeder
Wert zeigt Quelle, Zeitstempel, Einheit und Stale-Status. Optional ergänzt ein
EOD-Anbieter Aktien- und ETF-Kurse.

**C — vollständiger Eigenbau:** nur bei dokumentierten Lücken. Für einen
Nutzer genügen ein täglicher Collector, SQLite, eine read-only API und eine
lokale Weboberfläche. PostgreSQL, Redis und Queues werden erst bei mehreren
Nutzern, Intradaydaten oder vielen parallelen Jobs gerechtfertigt.

## Trade-offs and risks

- **Komfort gegen Datenhoheit:** Parqet automatisiert mehr, Portfolio
  Performance und Wealthfolio halten den Bestand lokal.
- **Reife gegen Erweiterbarkeit:** Portfolio Performance ist die konservative
  Referenz; Wealthfolio ist die bessere Entwicklungsbasis, aber volatiler.
- **Offizielle Werte gegen Proxys:** ETF-, CFD- oder indikative Feeds sind
  nicht identisch mit einem offiziellen Index und nicht für Abrechnung gedacht.
- **Kosten gegen Aktualität:** End-of-day ist günstig; globale Realtime-,
  Fixed-Income- und offizielle Indexfeeds können schnell dreistellig pro Monat
  oder individuell lizenzpflichtig werden.
- **Semantik:** Preisindex, Total-Return-Index, NAV, adjustierter Kurs,
  Rendite, Yield und Spread dürfen nicht vermischt werden.
- **Revisionen:** Makrodaten können später revidiert werden; `observation_date`,
  `fetched_at`, Quelle, Einheit und gegebenenfalls Vintage müssen gespeichert
  werden.
- **Datenschutz:** Brokerdateien gehören nicht in Git, Wiki, Chat oder Logs.
  Brokerpasswörter werden nicht gespeichert; API-Keys kommen aus `pass` und
  Laufzeit-Environment. Ein Self-hosted UI bleibt lokal oder hinter Tailscale.

## Open questions

1. Welche Broker und Banken müssen importiert werden?
2. Reicht eine lokale Mac-Anwendung oder soll das Cockpit im Homelab über
   Tailscale erreichbar sein?
3. Reicht End-of-day oder besteht ein konkreter Intradaybedarf?
4. Gehören neben Wertpapieren auch Konten, Immobilien, Edelmetalle und Krypto
   zum Zielbild?
5. Sind einzelne Anleihen im Depot, oder meint „Bond Market“ primär
   Staatsrenditen, Zinskurven und Credit Spreads?

Diese Antworten ändern die genaue Umsetzung, nicht aber die erste Empfehlung:
Portfolio Performance und Koyfin testen, erst danach Wealthfolio erweitern.

## Sources

Vollständige Evidenz, Preisstand, Primärquellen und Einzelbewertungen:

- [[_raw/research/personal-finance-market-dashboard/report]]

Verwandtes Grundlagenmaterial:

- [[personal-finance-market-foundations]]
