---
title: "Persönliches Finanz- und Marktdaten-Dashboard"
type: raw-research-report
tags: [research, finance, market-data, dashboard, self-hosting]
origin: research-workflow
created: 2026-08-21
---

# Persönliches Finanz- und Marktdaten-Dashboard

Recherche- und Preisstand: 2026-08-21. Preise und Produktumfang können sich
ändern. Dieser Bericht ist eine technische Entscheidungsvorlage und keine
Anlage-, Steuer- oder Rechtsberatung.

## Conclusion

### Kurzurteil

Christian sollte **nicht sofort einen vollständigen Portfolio-Tracker selbst
bauen**. Die schwierigen Teile sind nicht die Charts, sondern korrekte
Transaktionen, Cashflows, Kapitalmaßnahmen, Währungen, Instrumentzuordnung und
Datenlizenzen. Für einen belastbaren Start ist eine Trennung sinnvoll:

1. **Eigene Bestände und Performance:** Portfolio Performance lokal als
   verlässliches Portfolio-Buch oder alternativ Parqet, wenn der Komfort
   deutscher Brokerimporte wichtiger ist als vollständige Datenlokalität.
2. **Märkte, Zinsen und Bonds:** Koyfin Free als sofort nutzbares Market
   Cockpit. Es enthält Markt- und Makro-Dashboards, globale Staatsanleiherenditen
   und Zinskurven. TradingView ist die bessere Ergänzung, wenn Charting und
   Alerts wichtiger sind.
3. **Eigener Single-Pane-of-Glass:** Erst nach einem vierwöchigen Praxistest
   bauen. Der stärkste Kandidat dafür ist Wealthfolio als lokale, offene
   Portfolio-Basis plus ein eigenes, nur lesendes „Market Cockpit“-Add-on.
   Wealthfolio speichert lokal in SQLite und bietet ein berechtigungsbasiertes
   Add-on-System mit Zugriff auf Holdings, Performance und Marktdaten.

Die empfohlene Reihenfolge ist damit:

- **Jetzt und kostenlos:** Portfolio Performance + Koyfin Free.
- **Wenn deutsche Broker-Automatik zählt:** Parqet Basic/Plus + Koyfin Free.
- **Wenn ein eigenes, privates und optisch integriertes Dashboard wirklich
  gewünscht bleibt:** Wealthfolio lokal pilotieren und ein Add-on bauen.
- **Nur bei sehr speziellen Anforderungen:** eigener Daten- und
  Berechnungsstack.

### Warum zwei Systeme zunächst besser sind

Portfolio-Tracking und Marktbeobachtung sind unterschiedliche Probleme:

- Das Portfolio-System muss Transaktionen, Gebühren, Steuern, Ausschüttungen,
  Cashflows, Splits, mehrere Währungen und Performance korrekt verarbeiten.
- Das Markt-Cockpit muss viele Zeitreihen unterschiedlicher Herkunft anzeigen,
  deren Frequenz, Verzögerung und Bedeutung stark voneinander abweichen.

Keines der untersuchten Produkte ist in beiden Disziplinen gleichermaßen stark.
Portfolio Performance ist sehr gut bei lokaler Depotbuchhaltung und
Performance; Koyfin ist wesentlich stärker bei globalen Märkten, Zinskurven und
Makro. Eine vorschnelle Eigenentwicklung würde diese beiden reifen Systeme
schlechter nachbauen.

### Was „Bond Market“ im Dashboard bedeuten sollte

„Anleihen“ müssen in vier getrennte Anzeigen zerlegt werden:

1. **Staatsanleihe-Zinskurven:** z. B. 2, 5, 10 und 30 Jahre für Deutschland
   und die USA. Hier wird eine Rendite in Prozent gezeigt, kein Preis.
2. **Zinskurven-Steigung:** beispielsweise 10 Jahre minus 2 Jahre. Das zeigt die
   Kurvenform kompakter als vier Einzelwerte.
3. **Kreditrisiko:** Investment-Grade- und High-Yield-Spreads. Diese Daten sind
   häufig lizenzbehaftet; FRED veröffentlicht einige ICE-BofA-Reihen unter
   zusätzlichen Nutzungsbedingungen.
4. **Investierbare Bond-Positionen:** der tatsächliche Kurs, Stückzins,
   Fälligkeit und Yield-to-Maturity eines gehaltenen Bonds beziehungsweise der
   Marktpreis eines Bond-ETF. Das ist nicht dasselbe wie eine Zinskurve.

Für ein privates Markt-Cockpit sind offizielle Staatsanleihe-Zinsreihen leicht
und kostenlos zu beschaffen. Umfassende Kurse einzelner Unternehmensanleihen
sind deutlich schwieriger und gehören in einen bezahlten Feed oder in den
Brokerzugang.

## Evidence

### 1. Welche Werte das Dashboard wirklich zeigen sollte

Ein gutes Dashboard beantwortet in wenigen Sekunden vier Fragen:

1. Wie steht mein Vermögen heute?
2. Woher kommen Veränderung und Risiko?
3. Wie sieht das Markt- und Zinsregime aus?
4. Sind die angezeigten Daten aktuell und vergleichbar?

#### Empfohlenes Layout

```text
┌ Portfolio: NAV | Δ 1T | YTD | TTWROR 1J | Drawdown | Cash ┐
├ Meine Positionen ─────────────┬ Risiko & Allokation ────────┤
│ Top-/Flop-Beiträge            │ Assetklasse, Region, FX     │
│ Gewinne, Dividenden, Kupons   │ Konzentration, Drawdown     │
├ Aktienmärkte ─────────────────┼ Zinsen & Bonds ──────────────┤
│ Welt/USA/Europa/EM            │ EZB, €STR, Bund-/UST-Kurve   │
│ 1T, YTD, 52W-Drawdown         │ 2s10s, Realzins, Credit OAS  │
├ FX, Rohstoffe, Makro ─────────┴ Kalender / Datenqualität ────┤
│ EUR/USD, Gold, Brent | CPI, Arbeitsmarkt | Quelle/Stand/Lag  │
└──────────────────────────────────────────────────────────────┘
```

#### Portfolio-Kennzahlen

- Nettovermögen beziehungsweise investierbares Vermögen, getrennt nach
  Portfolio, Cash und sonstigen Vermögenswerten.
- Veränderung heute, MTD und YTD in Euro und Prozent.
- TTWROR für den Vergleich mit einem Benchmark und IRR für die persönliche,
  cashflow-gewichtete Rendite.
- Maximaler und aktueller Drawdown.
- Allokation nach Assetklasse, Region, Sektor und Währung.
- Top-Beiträge zur absoluten Wertveränderung, nicht nur prozentuale Gewinner.
- Konzentration der größten Positionen und Liquiditätsquote.
- Bei Bonds: Nennwert, Marktwert, Kupon, Fälligkeit, Duration und YTM, soweit
  diese Felder belastbar vorhanden sind.

Portfolio Performance dokumentiert TTWROR, IRR, Drawdown, Volatilität,
Semivarianz, Sharpe Ratio, Beitrags- und Heatmap-Widgets. Es berechnet die
Portfolio-Werte täglich und unterscheidet zeitgewichtete von
geldgewichteter Performance. Das ist ein starkes Argument, diese Rechnungen
nicht neu zu implementieren ([Performance-Dashboard](https://help.portfolio-performance.info/en/reference/view/reports/performance/dashboard/),
[Performance-Konzept](https://help.portfolio-performance.info/en/concepts/performance/),
jeweils abgerufen 2026-08-21).

#### Markt-Kennzahlen

- Globale Aktienblöcke statt einer langen Tickerwand: Welt, USA, Europa,
  Deutschland, Emerging Markets, Japan.
- Je Block: letzter Wert, 1 Tag, YTD, Abstand zum 52-Wochen-Hoch und Zeitstempel.
- EZB-Einlagensatz, €STR beziehungsweise Fed Funds als geldpolitischer Anker.
- Deutschland und USA: 2-, 5-, 10- und 30-jährige Rendite sowie 2s10s.
- US-Realzins 10 Jahre und optional Inflationserwartung.
- Investment-Grade- und High-Yield-Spread, wenn die Lizenz dies zulässt.
- EUR/USD, Gold und Brent als kompakte makroökonomische Ergänzung.

Nicht in Version 1 gehören Nachrichtenströme, Kursziele, technische Indikatoren,
Handelssignale, Prognosen und Tickdaten. Sie erzeugen visuelle Aktivität, aber
verbessern die tägliche Orientierung wenig.

### 2. Produkte: Was bereits existiert

| Produkt | Eigene Bestände | Deutsche Importe | Markt/Bonds | Datenhoheit | Aufwand | Urteil |
| --- | --- | --- | --- | --- | --- | --- |
| Portfolio Performance | sehr stark | sehr stark per PDF/CSV | begrenzt | lokal | niedrig | beste lokale Depotbuchhaltung |
| Parqet | stark | sehr stark, inklusive Autosync | mittel | Cloud | sehr niedrig | bequemste deutsche Option |
| Wealthfolio | stark | CSV; EU-Sync noch lückenhaft | über Provider erweiterbar | lokal/selbst gehostet | niedrig bis mittel | beste Basis für eigenes integriertes UI |
| Ghostfolio | gut | generischer Import | begrenzt/providerabhängig | selbst gehostet | mittel bis hoch | solide, aber für diesen Zweck unnötig schwer |
| Koyfin | einfache Portfolioansicht | keine deutsche Buchhaltungsstärke | sehr stark | Cloud | sehr niedrig | bestes sofortiges Markt-Cockpit |
| TradingView | einfache Portfolios/Watchlists | keine deutsche Buchhaltungsstärke | stark, besonders Charts | Cloud | sehr niedrig | beste Chart-/Alert-Ergänzung |
| OpenBB | kein persönliches Portfolio-Buch | keine | sehr stark als Adapter | lokal möglich | mittel bis hoch | Baustein, kein fertiger Tracker |

#### Portfolio Performance

Portfolio Performance ist kostenlos, quelloffen und für Windows, macOS und
Linux verfügbar. Es speichert die Daten in einer lokalen XML-Datei und kann CSV
oder JSON exportieren. Transaktionen, Steuern und Gebühren werden historisch
erfasst; historische Kurse können aus verschiedenen Quellen geladen werden.
Die Software unterstützt Fremdwährungskonten mit EZB-Wechselkursen
([offizielle Produktseite](https://www.portfolio-performance.info/en/),
abgerufen 2026-08-21).

Für Deutschland besonders wichtig: Die Dokumentation nennt PDF-Parser für mehr
als 90 Banken und Broker sowie CSV und Interactive-Brokers-Flex-Queries
([PDF-Import](https://help.portfolio-performance.info/en/reference/file/import/pdf-import/),
[Importübersicht](https://help.portfolio-performance.info/en/reference/file/import/),
abgerufen 2026-08-21).

Stärken:

- Lokale, portable Daten und kein Cloudkonto.
- Reife Performance- und Risikoanalyse.
- Gute deutsche PDF-Importabdeckung.
- Keine Betriebsinfrastruktur.

Schwächen:

- Desktop-zentriert; kein ideales Always-on-Web-Dashboard.
- Marktüberblick, Zinskurven und Makro sind nicht die Kernaufgabe.
- Die lokale Datei ist gut exportierbar, aber kein stabiler Service/API-Vertrag
  für ein frei entwickeltes Frontend.

#### Parqet

Parqet bietet einen kostenlosen Basic-Tarif, Plus für 11,99 Euro pro Monat und
Investor für 29,99 Euro pro Monat laut Preisseite am Recherchetag. PDF- und
CSV-Importe von über 50 Brokern sowie Autosync für Trade Republic, Scalable
Capital, ING, comdirect und Consorsbank werden ausgewiesen. Plus enthält unter
anderem X-Ray, Performancevergleiche und Steuer-/Dividendenansichten
([Preise und Funktionen](https://parqet.com/en/pricing), abgerufen 2026-08-21).

Parqet erklärt, Portfolio-, Login- und Zahlungsdaten getrennt in Deutschland zu
speichern. Beim PDF-Import werden nur transaktionsrelevante Felder übernommen.
Für Trade Republic und Scalable Capital verwendet Cloud Autosync QPLIX; die
Zugangsdaten werden laut Parqet ausschließlich in der Umgebung des lizenzierten
Partners eingegeben ([Datenschutz](https://parqet.com/en/data-protection),
abgerufen 2026-08-21).

Stärken:

- Sehr schneller Einstieg für deutsche Broker.
- Gute Web-/Mobiloberfläche und kein eigener Betrieb.
- Kostenlose Basisversion reicht zum Testen.

Schwächen:

- Portfolio- und Nutzungsdaten liegen bei einem Cloudanbieter.
- Kein Ersatz für ein globales Bond-/Makro-Terminal.
- Abhängigkeit von Produkt-, Preis- und Integrationsänderungen.

#### Wealthfolio

Wealthfolio ist AGPL-3.0-lizenziert, lokal-first und speichert Portfolio,
Transaktionen und Einstellungen in SQLite. Es gibt Desktop-Apps und ein
offizielles Docker-/Web-Deployment. Die Kernanwendung unterstützt Investments,
Net Worth, Performance, mehrere Währungen, CSV-Import und lokale Backups
([GitHub-Projekt](https://github.com/wealthfolio/wealthfolio),
[Einführung](https://wealthfolio.app/docs/introduction/), abgerufen 2026-08-21).

Für den konkreten Wunsch ist das Add-on-System entscheidend: TypeScript-/React-
Add-ons können eigene Seiten und Navigation bereitstellen und nach expliziter
Freigabe auf Portfolio, Holdings, Performance, Marktdaten, Netzwerk und Secrets
zugreifen. Berechtigungen werden statisch erkannt und dem Nutzer bei der
Installation angezeigt
([Add-on-Dokumentation](https://wealthfolio.app/docs/addons/),
[API-Referenz](https://wealthfolio.app/docs/addons/api-reference/),
abgerufen 2026-08-21).

Die eingebauten Kursquellen umfassen Yahoo Finance, Alpha Vantage, Finnhub,
MarketData.app, OpenFIGI, Börse Frankfurt, Metal Price API und einen US-Treasury-
Rechner. Pro Instrument sind Provider- und Symbolzuordnungen möglich. Eigene
JSON-, HTML- oder CSV-Quellen lassen sich konfigurieren
([Marktdatenkonzept](https://wealthfolio.app/docs/concepts/market-data-and-fx/),
[Custom Provider](https://wealthfolio.app/docs/guide/custom-providers/),
abgerufen 2026-08-21).

Das optionale Wealthfolio Connect bietet täglich aktualisierte, lesende
Brokerverbindungen und Ende-zu-Ende-verschlüsselten Gerätesync. Essentials kostet
laut aktueller Seite 7,99 US-Dollar pro Monat. Die Liste von über 35 Instituten
ist jedoch US-lastig; aus Europa werden unter anderem DEGIRO, Trading212 und Bux
genannt, nicht aber die wichtigsten deutschen Neobroker
([Connect](https://wealthfolio.app/connect/),
[unterstützte Broker](https://wealthfolio.app/connect/brokerages/),
abgerufen 2026-08-21).

Stärken:

- Lokale SQLite-Daten, Desktop oder Docker.
- Modernes UI und genau der nötige Erweiterungspunkt für ein eigenes Cockpit.
- Berechtigungs- und Secrets-Modell für Add-ons.
- Daten können als CSV, JSON oder vollständige SQLite-Datenbank gesichert werden
  ([Export und Backup](https://wealthfolio.app/docs/guide/data-export/)).

Schwächen:

- Jünger und schneller im Wandel als Portfolio Performance.
- Deutsche Brokerimporte sind weniger bequem.
- Einige eingebaute Provider oder konfigurierbare Scraper sind technisch
  praktisch, aber nicht automatisch vertraglich stabil oder zur automatischen
  Nutzung erlaubt.

**Einordnung:** Wealthfolio ist die beste Eigenbau-Basis, aber zunächst als
Pilot. Portfolio Performance bleibt vorerst die vertrauenswürdigere Referenz
für die historische Performance.

#### Ghostfolio

Ghostfolio ist ein quelloffener Web-Tracker für Aktien, ETFs und Krypto mit
Multi-Account-Unterstützung, Import/Export, Charts und PWA. Self-hosting wird
offiziell unterstützt. Der Stack benötigt jedoch PostgreSQL, Redis, NestJS und
Angular. Als Standarddatenquellen erscheinen unter anderem Yahoo Finance,
CoinGecko und manuelle Daten
([Projekt und Self-hosting](https://github.com/ghostfolio/ghostfolio),
abgerufen 2026-08-21).

Das ist ein deutlich größerer Betriebsfußabdruck als Wealthfolios lokale
SQLite-/Servervariante. Für einen privaten Single-User-Fall mit Wunsch nach
einem individuell eingebetteten Markt-Cockpit bietet Wealthfolio die passendere
Erweiterungsarchitektur.

#### Koyfin

Koyfin ist der stärkste „es gibt schon etwas“-Kandidat. Der kostenlose Tarif
enthält My Portfolios, Advanced Charting, Markt- und Makro-Dashboards, zwei
Watchlists, zwei Screens und zwei eigene Dashboards. Plus und Premium werden auf
der am Recherchetag auf „Annual“ stehenden Preisseite mit 39 beziehungsweise 79
US-Dollar pro Monat ausgewiesen
([Preise](https://www.koyfin.com/pricing/), abgerufen 2026-08-21).

Koyfin dokumentiert unter anderem globale Renditen, Währungen und Zinskurven.
Die Datenübersicht nennt Live-Staatsanleiherenditen für 45 Länder und
Zinskurven für 20 Länder. Für Aktienindizes ist die Semantik wichtig: Livewerte
für SPX, NDX und Dow werden laut Koyfin aus CFDs abgeleitet; andere globale
Aktienindizes sind End-of-day. Das sind nicht zwingend offizielle Indexfeeds
([Datenübersicht](https://www.koyfin.com/help/data-overview/),
[Bonds und Zinskurven](https://www.koyfin.com/help/global-bonds-yield-curves-fx/),
abgerufen 2026-08-21).

Koyfin kann eigene Holdings in Portfoliofeldern abbilden, ersetzt aber keine
deutsche Transaktionsbuchhaltung. Einige Capital-IQ-Daten dürfen nicht als CSV
exportiert werden. Es ist damit eine Oberfläche, keine verlässliche Quelle für
den eigenen Datenbestand.

#### TradingView

TradingView bietet eine sehr breite Marktabdeckung, globale Staatsanleihen,
Zinskurven, Bond-Screener und starke Charts. Die kostenlose Version reicht für
einen ersten Marktschirm; am Recherchetag begann der jährlich abgerechnete
Essential-Tarif bei 12,95 Euro pro Monat. Zusätzliche professionelle
Marktdatenabonnements können separat nötig werden
([Preise](https://www.tradingview.com/pricing/),
[Bond-Markt](https://www.tradingview.com/markets/bonds/),
abgerufen 2026-08-21).

TradingView ist dann sinnvoll, wenn Alerts, technische Charts und viele
Instrumente wichtiger sind als das makroökonomisch geordnete Cockpit von
Koyfin.

#### OpenBB

OpenBB ist kein fertiges persönliches Portfolio-Buch, sondern ein modularer
Datenzugriff. Die Open Data Platform standardisiert Provider und kann über
Python oder FastAPI genutzt werden. Öffentliche Provider-Erweiterungen umfassen
unter anderem ECB, FRED, Federal Reserve, US Government, IMF und OECD; andere
Provider benötigen Schlüssel oder bezahlte Konten. OpenBB hostet selbst keine
Daten und weist darauf hin, dass Provider-Endpunkte je nach installierten
Erweiterungen und Abonnements variieren
([Developer Guide](https://docs.openbb.co/platform/developer_guide),
[Provider](https://docs.openbb.co/odp/python/extensions/providers),
abgerufen 2026-08-21).

Für einen späteren Eigenbau ist OpenBB ein nützlicher Adapter, besonders für
Zinskurven und Makro. Die dokumentierte Yield-Curve-Schnittstelle kann ECB,
Federal Reserve, FRED und weitere Provider normalisieren
([Yield Curve](https://docs.openbb.co/odp/python/reference/fixedincome/government/yield_curve)).
Die Kernlogik sollte dennoch Source-IDs und Rohdaten je Anbieter speichern,
damit ein Wechsel des Wrappers nicht die Nachvollziehbarkeit zerstört.

### 3. Datenquellen: Was belastbar, kostenlos oder teuer ist

| Datenbereich | Bevorzugte Quelle | Kosten | Frequenz | Wichtigste Grenze |
| --- | --- | --- | --- | --- |
| Eigene Transaktionen | Broker-PDF/CSV; PP/Parqet-Import | meist frei | ereignisbasiert | Import muss reconciled werden |
| ECB-Sätze und EUR-FX | ECB Data Portal | frei | täglich/ereignisbasiert | SDMX-Metadaten beachten |
| Deutsche Bund-Kurve | Bundesbank SDMX | frei | täglich/monatlich je Reihe | korrekte Reihe und Methode wählen |
| Einzelne Bundeswertpapiere | Bundesbank Referenzpreise/Renditen nach ISIN | frei | börsentäglich | kein universeller Corporate-Bond-Feed |
| US-Treasury-Kurve | US Treasury XML/CSV | frei | täglich | Par Yield ist kein Bondpreis |
| EU-Makro | Eurostat API | frei | je Veröffentlichung | Revisionen und Frequenzen |
| US/globales Makro | FRED API | frei mit Key | je Reihe | Quellrechte je Serie; Attribution |
| Instrument-Mapping | ISIN + MIC; OpenFIGI | frei | bei Onboarding | Ticker allein ist nicht eindeutig |
| Globale Aktien/ETFs EOD | EODHD oder bestehender Trackerfeed | ab 19,99 USD/Monat | EOD | indikativ, nicht börsenoffiziell |
| Kleine Watchlist EOD | Alpha Vantage | frei bis 25 Calls/Tag | standardmäßig EOD | geringe Quote; Realtime US bezahlt |
| Globale Realtime-/EU-Daten | Twelve Data | 79/229 USD+ je Tarif | EOD bis realtime | für Privatcockpit meist zu teuer |
| Offizielle Indexlevels | Indexanbieter/lizenzierter Terminalanbieter | Angebot/Lizenz | EOD/realtime | Marken- und Datenrechte |
| Credit Spreads | FRED/ICE eingeschränkt oder bezahlter Feed | gemischt | meist täglich | zusätzliche ICE-Bedingungen |

#### Offizielle Zins-, FX- und Makrodaten

Das ECB Data Portal bietet eine SDMX-2.1-REST-Schnittstelle für Daten und
Metadaten. Abfragen können Zeiträume, Aktualisierungen, letzte Beobachtungen und
CSV/JSON-Formate steuern
([ECB API Overview](https://data.ecb.europa.eu/help/api/overview),
[ECB Data API](https://data.ecb.europa.eu/help/api/data), abgerufen 2026-08-21).

Die Bundesbank bietet ebenfalls eine HTTPS-REST-API mit SDMX-JSON, SDMX-CSV und
weiteren Formaten. Die Datenbank enthält unter anderem tägliche Renditen
aktueller Bundeswertpapiere, Svensson-Zinskurven und börsentäglich aktualisierte
Referenzpreise und Renditen einzelner Bundeswertpapiere nach ISIN
([Bundesbank SDMX API](https://www.bundesbank.de/en/statistics/time-series-databases/help-for-sdmx-web-service/web-service-interface-data),
[Bund-Zinsstruktur](https://www.bundesbank.de/de/statistiken/geld-und-kapitalmaerkte/zinssaetze-und-renditen/taegliche-zinsstruktur-fuer-boersennotierte-bundeswertpapiere-650724),
[Preise/Renditen nach ISIN](https://www.bundesbank.de/de/statistiken/geld-und-kapitalmaerkte/zinssaetze-und-renditen/kurse-renditen-der-bundeswertpapiere/kurse-und-renditen-boersennotierter-bundeswertpapiere-772408),
abgerufen 2026-08-21).

Das US Treasury veröffentlicht tägliche Par-Yield-Curve-Rates als CSV und XML;
der XML-Feed hat eine dokumentierte GET-Schnittstelle
([Daily Treasury Rates](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve),
[XML Feed](https://home.treasury.gov/treasury-daily-interest-rate-xml-feed),
abgerufen 2026-08-21).

Eurostat stellt kostenfreie REST-APIs in JSON-stat und SDMX bereit. Die
Datensätze werden bei neuen Daten zweimal täglich aktualisiert; ältere
Versionen werden in der Standarddatenbank nicht aufbewahrt
([Eurostat API](https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-introduction),
abgerufen 2026-08-21). Für ein revisionssensitives Dashboard sollte der eigene
Collector deshalb jede tatsächlich verwendete Beobachtung mit `fetched_at`
speichern.

FRED eignet sich für Makro, Realzinsen, Spreads und viele US-Zeitreihen. Die API
benötigt einen Schlüssel. In einer eigenen Anwendung muss der Hinweis „This
product uses the FRED API but is not endorsed or certified by the Federal
Reserve Bank of St. Louis“ angezeigt werden; außerdem gelten Rechte und Hinweise
der jeweiligen Ursprungsserie
([FRED API Terms](https://fred.stlouisfed.org/docs/api/terms_of_use.html),
[Series Observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html),
abgerufen 2026-08-21).

#### Instrument-Identität

Ein Ticker ist nicht ausreichend. Dasselbe Wertpapier kann an mehreren Börsen
und in mehreren Währungen gehandelt werden. Das minimale kanonische Modell ist:

- ISIN für das Finanzinstrument;
- MIC für den Handelsplatz;
- Handelswährung;
- Provider-spezifischer Symbolalias;
- bei Bedarf FIGI/Composite FIGI für Mapping und Aggregation.

ISO 6166 definiert die ISIN-Struktur; ISO 10383 die Market Identifier Codes
([ISO 6166](https://www.iso.org/standard/78502.html),
[ISO 10383](https://www.iso.org/standard/61067.html)). OpenFIGI bietet eine
freie Mapping-API; ohne Schlüssel gelten 25 Requests pro Minute und 10 Jobs pro
Request, mit Schlüssel höhere Grenzen
([OpenFIGI API](https://www.openfigi.com/api/documentation),
abgerufen 2026-08-21).

#### Aktien-, ETF- und Indexdaten

EODHD ist für ein privates EOD-Cockpit der preislich plausibelste einheitliche
Feed. Der globale EOD-Tarif wird aktuell mit 19,99 US-Dollar monatlich oder 199
US-Dollar jährlich ausgewiesen; die freie Stufe erlaubt 20 Calls pro Tag und
nur ein Jahr Historie. EODHD nennt 70 Börsen und virtuelle Bereiche für
Government Bonds und Money Markets
([Preise](https://eodhd.com/pricing),
[Coverage](https://eodhd.com/financial-apis/exchanges-api-list-of-tickers-and-trading-hours),
abgerufen 2026-08-21).

Die entscheidende Einschränkung steht auf derselben Preisseite: Viele Preise
werden aus OTC-, Peer-to-peer- und Trading-Platform-Quellen aggregiert und sind
nicht notwendigerweise börsenoffizielle Realtimekurse. Sie sind für ein
persönliches EOD-Dashboard plausibel, nicht für Handel, Abrechnung oder die
Reconciliation des Brokerwerts.

Alpha Vantage unterstützt globale Aktien und ETFs, aber die Standardgrenze
liegt bei 25 API-Requests pro Tag. Globale Quote-Antworten sind standardmäßig
End-of-day; US-Realtime und 15-Minuten-Verzögerung benötigen Premium und ein
Entitlement. Treasury-Yields sind ebenfalls verfügbar
([Dokumentation](https://www.alphavantage.co/documentation/),
[Premium](https://www.alphavantage.co/premium/), abgerufen 2026-08-21).
Für eine kleine Watchlist kann das reichen; für viele Instrumente oder robuste
Backfills ist die Quote zu knapp.

Twelve Data bietet einen sehr breiten, sauberen API-Vertrag. Die kostenlose
Stufe nennt 800 Calls pro Tag, aber nur drei Märkte; der Hobby-Tarif Grow kostet
aktuell 79 US-Dollar monatlich. Realtime-EU- und Fixed-Income-Daten erscheinen
erst im Pro-Tarif für 229 US-Dollar monatlich
([Preise](https://twelvedata.com/pricing),
[API](https://twelvedata.com/docs), abgerufen 2026-08-21). Das ist technisch
attraktiv, für ein langfristiges Privatdashboard aber erst gerechtfertigt, wenn
der konkrete Nutzen von Realtime nachgewiesen ist.

Offizielle Indexlevels sind ein eigener Lizenzbereich. S&P DJI bietet
lizenzierte End-of-day- und Realtime-Pakete, APIs und SFTP an; Preise werden
nicht als günstiger Self-service-Tarif ausgewiesen
([Data & Index Licensing](https://www.spglobal.com/spdji/en/about-us/data-index-licensing/),
[API Data Solutions](https://www.spglobal.com/spdji/en/landing/topic/api-data-solutions/),
abgerufen 2026-08-21).

**Empfohlene Inferenz:** Für das private Dashboard investierbare ETF-Proxys
verwenden, wenn es um die Performance eines Marktsegments geht. Ein liquider
ETF-Kurs ist einfacher legal zu beziehen und entspricht dem tatsächlich
investierbaren Total-Return-Erlebnis besser als ein Price Index. Der exakte
Indexname, das ETF-Symbol und die Abweichung müssen sichtbar dokumentiert
werden. Für reine Marktlevels Koyfin oder TradingView als lizenzierte Anzeige
nutzen, statt deren Daten in den eigenen Stack zu kopieren.

#### Credit Spreads und FRED-Rechte

FRED führt zum Beispiel den ICE BofA US High Yield Option-Adjusted Spread. Die
Reihe ist täglich, aber seit April 2026 auf drei Jahre Beobachtungen begrenzt und
trägt zusätzliche ICE-Nutzungsbedingungen
([BAMLH0A0HYM2](https://fred.stlouisfed.org/series/BAMLH0A0HYM2),
abgerufen 2026-08-21). Das zeigt exemplarisch: Eine FRED-API-Antwort ist nicht
automatisch gemeinfrei. Der Collector muss Quellhinweis, Lizenznotiz und
zulässige Nutzung pro Serie speichern.

### 4. Drei umsetzbare Reifegrade

#### Reifegrad A: Sofort nutzbar, kein Eigenbau

**Stack:** Portfolio Performance + Koyfin Free; optional TradingView Free.

Vorgehen:

1. Brokerabrechnungen oder CSV in Portfolio Performance importieren.
2. Broker-Endbestand und Cashsaldo nach jedem Import abgleichen.
3. Ein Portfolio-Dashboard für TTWROR, IRR, Drawdown, Allokation und Beiträge
   konfigurieren.
4. In Koyfin zwei Dashboards anlegen: „Global Markets“ und „Rates & Credit“.
5. Keine echten Stückzahlen in Koyfin hinterlegen, wenn der Cloudanbieter nur
   die Märkte und nicht das persönliche Portfolio sehen soll.

Kosten: 0 Euro. Zeit: ungefähr zwei bis vier Stunden plus Datenbereinigung.

Das ist die klare Empfehlung für die ersten vier Wochen.

#### Reifegrad B: Privates integriertes Dashboard

**Stack:** Wealthfolio Desktop oder selbst gehostet + eigenes
`market-cockpit`-Add-on.

Das Add-on liest Holdings und Performance über die freigegebenen Wealthfolio-
APIs und lädt nur die benötigten offiziellen Marktserien. Die ersten Quellen:

- ECB: Leitzinsen und EUR-FX;
- Bundesbank: deutsche Bund-Zinskurve und bei Bedarf gehaltene
  Bundeswertpapiere nach ISIN;
- US Treasury: US-Par-Yield-Curve;
- Eurostat/FRED: wenige ausgewählte Makroreihen;
- Wealthfolio-eigene Provider oder EODHD: Aktien- und ETF-EOD-Kurse.

Das Add-on bleibt lesend für Portfolio- und Transaktionsdaten. Es darf keine
Trades auslösen und keine Brokerzugangsdaten kennen. Netzwerkzugriffe werden auf
explizite Hosts begrenzt; API-Keys liegen im vorgesehenen Secrets-Speicher.

Kosten:

- Wealthfolio: 0 Euro;
- offizielle Statistik-/Zinsfeeds: 0 Euro;
- optional EODHD All World EOD: 19,99 US-Dollar monatlich;
- optional Wealthfolio Connect Essentials: 7,99 US-Dollar monatlich, falls ein
  unterstützter Broker genutzt wird.

Risiko: Wealthfolio ist in aktiver Entwicklung. Die Add-on-API sollte vor einer
größeren Implementierung mit einem kleinen Read-only-Prototyp validiert werden.

#### Reifegrad C: Vollständiger Eigenbau

Nur sinnvoll, wenn Wealthfolio/Portfolio Performance nach dem Pilot konkrete,
dauerhafte Grenzen zeigen.

KISS-Architektur:

```text
Broker-PDF/CSV ──> Import/Validation ─┐
ECB/Bundesbank/Treasury/FRED ────────┼─> SQLite ─> read-only API ─> Dashboard
EOD equity/ETF provider ─────────────┘       │
                                             └─> encrypted backup
```

Für einen einzelnen Nutzer reichen SQLite, ein täglicher Python-Collector und
eine lokale Weboberfläche. PostgreSQL, Redis und eine Queue sind erst nötig,
wenn mehrere Nutzer, Intradaydaten oder viele parallele Jobs hinzukommen.
OpenBB kann als Normalisierungsadapter dienen, sollte aber nicht die einzige
Schicht sein, die Source-IDs und Herkunft kennt.

Minimales Datenmodell:

| Tabelle | Zweck | Zentrale Felder |
| --- | --- | --- |
| `instruments` | kanonische Instrumente | ISIN, FIGI, MIC, Typ, Währung |
| `provider_symbols` | Provider-Mapping | Instrument, Provider, Symbol |
| `accounts` | Depots/Cashkonten | Name, Typ, Basiswährung |
| `transactions` | unveränderliche Buchungen | Typ, Datum, Menge, Preis, Gebühren, Steuern |
| `prices` | Wertpapierkurse | Instrument, Datum, raw/adjusted/NAV, Quelle |
| `fx_rates` | Umrechnung | Paar, Datum, Kurs, Quelle |
| `series` | Makro-/Zinsmetadaten | Source-ID, Einheit, Frequenz, Lizenzhinweis |
| `observations` | Zeitreihenwerte | Serie, Beobachtungsdatum, Wert, Vintage |
| `valuation_snapshots` | täglicher Depotstand | Konto, Datum, Marktwert, Cash |
| `ingestion_runs` | Datenqualität | Start/Ende, Status, Zeilen, Fehler, `as_of` |

Jeder angezeigte Wert braucht mindestens:

- `observation_date` oder `as_of`;
- `fetched_at`;
- Quelle und Serien-/Instrument-ID;
- Währung und Einheit;
- Preisart (`raw`, `adjusted`, `NAV`, `yield`, `spread`);
- erwartete Frequenz und Stale-Schwelle.

Ohne diese Metadaten ist ein optisch schönes Dashboard finanziell
mehrdeutig.

### 5. Aktualisierungstakt

Realtime ist für den beschriebenen Zweck nicht nötig. Ein sinnvolles Schema:

| Daten | Aktualisierung | Stale-Warnung |
| --- | --- | --- |
| Portfolio-Transaktionen | nach Brokerimport | wenn Endbestand nicht reconciled |
| Aktien/ETF EOD | nach jeweiligem Börsenschluss | nach 2 Handelstagen |
| ECB/Bundesbank/Treasury | täglich morgens | nach 3 Werktagen |
| FX-Referenzkurs | täglich | nach 2 Werktagen |
| CPI/Arbeitsmarkt | täglich auf neue Publikation prüfen | nach erwartetem Release |
| Depot-NAV-Snapshot | täglich nach Kursimport | wenn Kursabdeckung < 100 % |

Eine sichtbare Datenqualitätsleiste sollte Anzahl veralteter Positionen,
fehlende Kurse, letzte erfolgreiche Jobs und Abweichung zum Broker-Endbestand
zeigen.

### 6. Datenschutz und Betrieb

- Broker-PDFs und CSVs sind sensible Rohdaten. Sie gehören nicht in Git, Wiki,
  Chat, Logaggregation oder unverschlüsselte Cloudverzeichnisse.
- Die erste Version verwendet manuelle Dateien; keine gespeicherten
  Brokerpasswörter.
- Wenn Synchronisierung später nötig ist, OAuth oder einen explizit lesenden,
  regulierten Aggregator bevorzugen. Anbieterumfang und übertragene Felder
  vorher prüfen.
- API-Schlüssel über `pass` und Laufzeit-Environment bereitstellen, nicht in
  Compose-Dateien oder Repositories.
- Selbst gehostete Weboberflächen nur lokal oder über Tailscale erreichbar
  machen; keine öffentliche Portfreigabe.
- SQLite-/Portfolio-Datei regelmäßig verschlüsselt sichern und Restore testen.
- Logs enthalten technische Jobdaten, aber keine Bestände, Beträge,
  Transaktionsbeschreibungen oder Dokumentinhalte.
- Nach jedem Import: Stückzahlen, Cash und Gesamtwert gegen die Brokeranzeige
  abgleichen; Differenzen sichtbar halten, nicht still korrigieren.

### 7. Konkreter Entscheidungs- und Umsetzungsplan

#### Phase 0: Anforderungen beobachten, eine Woche

- Portfolio Performance installieren und einen repräsentativen Broker
  importieren.
- Koyfin Free mit zwei Dashboards aufsetzen.
- Täglich notieren, welche Information tatsächlich fehlt.

Abbruchkriterium für Eigenbau: Wenn Portfolio Performance + Koyfin alle
regelmäßig genutzten Fragen beantworten, wird nichts gebaut.

#### Phase 1: Datenqualität, ein bis zwei Wochen

- Alle Depots/Cashkonten importieren.
- ISIN, Handelsplatz, Währung und Kursquelle je Position prüfen.
- TTWROR und IRR nicht mit einfachem Gewinn/Einstand verwechseln.
- Für Marktbenchmarks ETF-Proxys bewusst auswählen und dokumentieren.
- Bond-Kurve Deutschland/USA mit offiziellen Quellen festlegen.

#### Phase 2: Single-Pane-Prototyp, zwei bis vier Tage

- Wealthfolio lokal parallel mit einem kleinen Datenbestand testen.
- Ein Add-on mit nur drei externen Quellen bauen: ECB, Bundesbank und US
  Treasury.
- Die Dashboard-Seite mit Portfolio-Kopfzeile, Equity-Proxys und zwei
  Zinskurven umsetzen.
- Provider, Zeitstempel und Verzögerung auf jeder Kachel anzeigen.

#### Phase 3: Entscheidung nach vier Wochen

- Wealthfolio wird führendes System, wenn Importe, Reconciliation und
  Performance gegenüber Portfolio Performance stimmen.
- Andernfalls bleibt Portfolio Performance führend und das Cockpit zeigt nur
  Marktwerte sowie einen täglich exportierten Portfolio-NAV.
- Ein kompletter Eigenbau beginnt nur, wenn ein konkretes Defizit weder durch
  PP, Parqet, Wealthfolio noch Koyfin lösbar ist.

## Trade-offs and risks

### Datenaktualität gegen Kosten

End-of-day reicht für langfristige Allokation, Rendite- und Risikobetrachtung.
Realtime erhöht Gebühren, Lizenzkomplexität, Datenvolumen und Betriebsaufwand,
ohne den Nutzen eines persönlichen Vermögenscockpits entsprechend zu erhöhen.

### Komfort gegen Datenhoheit

- Parqet ist bei deutschen Brokern bequemer, aber cloudbasiert.
- Portfolio Performance hält alles lokal, benötigt aber manuelle Importe.
- Wealthfolio ist lokal und moderner, hat derzeit weniger passende deutsche
  Brokerverbindungen.

### Reife gegen Erweiterbarkeit

- Portfolio Performance ist der konservative, reife Referenzpunkt.
- Wealthfolio ist die attraktivste Entwicklungsplattform, aber jünger und
  API-/Schemaänderungen sind wahrscheinlicher.
- Ghostfolio ist reif als Webservice, bringt jedoch für einen Single User mehr
  Infrastruktur mit.

### Offizielle Werte gegen Proxys

- Ein ETF-Proxy ist investierbar und günstig als Kurs verfügbar, aber nicht
  identisch zum offiziellen Indexlevel.
- Koyfin dokumentiert einige Live-Indexwerte als CFD-abgeleitet.
- EODHD weist seine Daten als indikativ und nicht zwingend börsenoffiziell aus.
- Für Abrechnung und Bestandsabgleich ist deshalb immer der Broker oder die
  offizielle Emittenten-/Börsenquelle maßgeblich.

### Datenrevisionen und Semantik

Makrodaten werden revidiert. Eurostat hält in der Standard-API nur die aktuelle
Version; FRED kann Vintages abbilden. Ein Dashboard ohne Vintage-/Fetch-Datum
kann historische Signale rückwirkend verändern. Ebenso müssen Preisindex,
Total-Return-Index, adjustierter Aktienkurs, NAV, Rendite und Spread als
unterschiedliche Messgrößen behandelt werden.

### Lizenzrisiko

Ein kostenlos erreichbarer Webwert ist nicht automatisch frei automatisierbar
oder weiterverteilbar. Besonders Indexlevel, Credit-Spreads und Realtimekurse
können zusätzliche Rechte tragen. Das private Dashboard sollte nicht öffentlich
geteilt werden; jede Quelle erhält einen gespeicherten Lizenz- und
Attributionshinweis. Scraping wird nicht als Standardarchitektur empfohlen.

## Open questions

Vor der konkreten Implementierung sind fünf Entscheidungen erforderlich:

1. Welche Broker und Banken sollen importiert werden?
2. Soll das Dashboard nur auf dem Mac laufen oder dauerhaft im Homelab über
   Tailscale erreichbar sein?
3. Reicht End-of-day oder gibt es einen belegbaren Intraday-/Realtime-Bedarf?
4. Sollen nur börsennotierte Assets oder auch Konten, Immobilien, Edelmetalle
   und Krypto enthalten sein?
5. Sind einzelne Anleihen im Depot, oder meint „Bond Market“ primär globale
   Staatsrenditen, Zinskurven und Credit-Spreads?

Diese Antworten ändern die genaue Produktauswahl, aber nicht die
Grundempfehlung: erst Portfolio Performance + Koyfin testen, dann bei echtem
Integrationsbedarf Wealthfolio erweitern.

## Sources

Alle Quellen wurden am 2026-08-21 abgerufen, sofern nicht anders angegeben.

### Portfolio- und Dashboard-Produkte

- Portfolio Performance: https://www.portfolio-performance.info/en/
- Portfolio Performance Import: https://help.portfolio-performance.info/en/reference/file/import/
- Portfolio Performance PDF import: https://help.portfolio-performance.info/en/reference/file/import/pdf-import/
- Portfolio Performance dashboard: https://help.portfolio-performance.info/en/reference/view/reports/performance/dashboard/
- Portfolio Performance performance concepts: https://help.portfolio-performance.info/en/concepts/performance/
- Parqet pricing: https://parqet.com/en/pricing
- Parqet privacy: https://parqet.com/en/data-protection
- Wealthfolio repository: https://github.com/wealthfolio/wealthfolio
- Wealthfolio introduction: https://wealthfolio.app/docs/introduction/
- Wealthfolio market data: https://wealthfolio.app/docs/concepts/market-data-and-fx/
- Wealthfolio custom providers: https://wealthfolio.app/docs/guide/custom-providers/
- Wealthfolio add-ons: https://wealthfolio.app/docs/addons/
- Wealthfolio export and backup: https://wealthfolio.app/docs/guide/data-export/
- Wealthfolio Connect: https://wealthfolio.app/connect/
- Wealthfolio supported brokerages: https://wealthfolio.app/connect/brokerages/
- Ghostfolio repository: https://github.com/ghostfolio/ghostfolio
- Koyfin pricing: https://www.koyfin.com/pricing/
- Koyfin data overview: https://www.koyfin.com/help/data-overview/
- Koyfin bonds and yield curves: https://www.koyfin.com/help/global-bonds-yield-curves-fx/
- TradingView pricing: https://www.tradingview.com/pricing/
- TradingView bonds: https://www.tradingview.com/markets/bonds/
- OpenBB developer guide: https://docs.openbb.co/platform/developer_guide
- OpenBB providers: https://docs.openbb.co/odp/python/extensions/providers
- OpenBB yield curves: https://docs.openbb.co/odp/python/reference/fixedincome/government/yield_curve

### Official and commercial data sources

- ECB API overview: https://data.ecb.europa.eu/help/api/overview
- ECB data API: https://data.ecb.europa.eu/help/api/data
- Bundesbank SDMX API: https://www.bundesbank.de/en/statistics/time-series-databases/help-for-sdmx-web-service/web-service-interface-data
- Bundesbank Bund yield curve: https://www.bundesbank.de/de/statistiken/geld-und-kapitalmaerkte/zinssaetze-und-renditen/taegliche-zinsstruktur-fuer-boersennotierte-bundeswertpapiere-650724
- Bundesbank listed federal securities: https://www.bundesbank.de/de/statistiken/geld-und-kapitalmaerkte/zinssaetze-und-renditen/kurse-renditen-der-bundeswertpapiere/kurse-und-renditen-boersennotierter-bundeswertpapiere-772408
- US Treasury daily rates: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve
- US Treasury XML feed: https://home.treasury.gov/treasury-daily-interest-rate-xml-feed
- Eurostat API: https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-introduction
- FRED API terms: https://fred.stlouisfed.org/docs/api/terms_of_use.html
- FRED observations API: https://fred.stlouisfed.org/docs/api/fred/series_observations.html
- FRED ICE BofA US High Yield OAS: https://fred.stlouisfed.org/series/BAMLH0A0HYM2
- OpenFIGI API: https://www.openfigi.com/api/documentation
- ISO 6166: https://www.iso.org/standard/78502.html
- ISO 10383: https://www.iso.org/standard/61067.html
- Alpha Vantage documentation: https://www.alphavantage.co/documentation/
- Alpha Vantage premium: https://www.alphavantage.co/premium/
- Twelve Data pricing: https://twelvedata.com/pricing
- Twelve Data API: https://twelvedata.com/docs
- EODHD pricing: https://eodhd.com/pricing
- EODHD coverage: https://eodhd.com/financial-apis/exchanges-api-list-of-tickers-and-trading-hours
- S&P data and index licensing: https://www.spglobal.com/spdji/en/about-us/data-index-licensing/
- S&P API data solutions: https://www.spglobal.com/spdji/en/landing/topic/api-data-solutions/
