---
title: "Christians Framework Laptop 13 Pro"
type: wiki-page
tags: [framework, notebook, hardware, linux, ssd]
state: draft
created: 2026-10-03
sources:
  - _raw/conversations/2026-10-03--framework-notebook-konfiguration.md
  - _raw/sources/2026-10-03--framework-laptop-13-pro-intel-specs.md
  - _raw/research/framework-notebook-ssd-type--shallow/report.md
  - _raw/research/framework-notebook-gen4-ssd-shortlist--shallow/report.md
  - _raw/research/framework-notebook-ssd-fit--shallow/report.md
  - _raw/research/framework-notebook-gen4-more-options--shallow/report.md
  - _raw/conversations/2026-10-03--framework-ssd-auswahl-und-preisabgleich.md
---

# Christians Framework Laptop 13 Pro

## Zusammenfassung

Christians neues Notebook ist ein **Framework Laptop 13 Pro DIY Edition mit
Intel Core Ultra X7 358H und 32 GB LPCAMM2 LPDDR5X**. Die von Christian
vorgelegte Bestellübersicht bestätigt diese Konfiguration. Eine SSD wird noch
gesucht. Stand: 3. Oktober 2026; Wiki-Entwurf zur menschlichen Prüfung.

## Bestellte Konfiguration

| Bestandteil | Bestätigte Angabe |
| --- | --- |
| Modell | Framework Laptop 13 Pro DIY Edition |
| CPU | Intel Core Ultra X7 358H |
| RAM | 32 GB LPCAMM2 LPDDR5X |
| Display | 2.8K Touchscreen |
| Akku | 74 Wh laut Bestellung |
| Einfassung | Translucent Black |
| Tastatur | US English – Graphite – Gray/Black |
| Erweiterungskarten | 4 × USB-C, Aluminum – Graphite |
| Zubehör | Framework Screwdriver inklusive |
| Warranty | 2 Year laut Bestellübersicht |
| SSD | Keine in der vorgelegten Übersicht aufgeführt; Auswahl offen |

Bestellt am **19. Juli 2026**. Die am 3. Oktober vorgelegte Übersicht zeigt
**Vorbestellung aufgegeben, Batch 16 – Versand im Oktober**. Das ist ein
geplanter Versandzeitraum, keine Versand- oder Lieferbestätigung.

Christian sagt, dass er die 32 GB RAM nun hat. Ob bereits separat vorhanden,
eingebaut oder auf die bestellte Konfiguration bezogen, bleibt offen.

## Geprüfte Herstellerangaben

Die [offiziellen Spezifikationen](https://frame.work/laptop13pro?tab=specs)
nennen für die Intel-X7-Variante:

- 16 CPU-Kerne/Threads (4 P + 8 E + 4 LPE), bis 4,8 GHz und Intel Arc B390.
- LPCAMM2 bis 7467 MT/s; angebotene RAM-Kapazitäten bis 64 GB.
- 13,5-Zoll-Touchdisplay mit 2880 × 1920 Pixeln, 30–120 Hz und typisch 700 Nits.
- 74,45-Wh-Akku, haptisches Touchpad und CNC-Aluminiumgehäuse.
- Thunderbolt 4, DisplayPort 2.1 und USB-PD auf allen vier Erweiterungsslots.

## Grundlage für die SSD-Auswahl

Die [SSD-Austauschanleitung von Framework](https://guides.frame.work/Guide/Storage-%2BSSD%2BReplacement%2Bfor%2BFramework%2BLaptop%2B13%2BPro/763)
bestätigt **M.2 2280 NVMe** als interne SSD-Bauform. Framework bietet für die
Intel-Variante PCIe-5.0-SSDs bis 2 TB und PCIe-4.0-SSDs bis 8 TB an und
erlaubt eigene SSDs. Diese Angebotsgrößen sind keine pauschalen
Kompatibilitätsgrenzen.

Für doppelseitige SSDs und Modelle mit Heatspreader gelten besondere
Einbauhinweise. Vor einem Einbau die vollständige Herstelleranleitung prüfen.
Das konkrete SSD-Modell und Budget sind noch offen. Christian bevorzugt nun
2 TB; 1 TB bleibt eine Ausweichoption.

### Recherchestand zur SSD, 3. Oktober 2026

Empfohlene Ausgangsklasse: **PCIe 4.0 x4, TLC-NAND, effizientes Client-Design,
vorzugsweise einseitig und ohne zusätzlichen Kühlkörper**. Eine gute DRAMlose
SSD mit HMB genügt als Ausgangspunkt für normale Entwicklung. Für intensive
VM-/Datenbank-I/O kann eigener DRAM interessant sein. Diese Einordnung ist
eine Empfehlung, keine bestätigte Kaufentscheidung.

**Erster Prüfkandidat: SN7100 2 TB.** Der
[Konfigurator für genau die Intel-Pro-DIY-Variante](https://frame.work/products/laptop13pro-diy-intel-ultra-3/body/new)
führt SN7100 mit 1 TB und 2 TB auf; die Passung ist damit direkt durch
Framework belegt. Weitere Kandidaten sind 990 EVO Plus, NM790 und 990 PRO.
KIOXIA EXCERIA PLUS G3 und SK hynix Platinum P41 haben laut Hersteller
einseitige M.2-2280-Bestückung; deren Passung ist aus den Spezifikationen
abgeleitet, nicht im konkreten Notebook getestet.

Der direkte Preisabgleich vom 3. Oktober zeigte für SN7100 2 TB ab 279 EUR
exklusive Versand. Das ist eine vergängliche Momentaufnahme; vor Kauf neu
prüfen. Der von einer externen Recherche genannte Lexar-M7-2-TB-Preis von
227,99 EUR war nicht bestätigt: Die geöffnete Geizhals-Seite zeigte keine
Angebote in der gewählten Region. Herstellerdaten und Passung der M7 sind offen.

Es gibt keine vergleichbaren Framework-Messungen zur Energie oder Temperatur
dieser Auswahl. PCIe-Generation, eigener DRAM oder HMB allein sind kein
verlässlicher Ersatz dafür. Ein Auslagern schwerer Workloads auf einen Server
ist in diesem Gespräch nicht bestätigt und wird nicht als Kaufargument benutzt.

## Bisheriger Nutzungskontext

Die persönliche Notiz `personal/notes/framework-13-pro.md` vom 11. Juli 2026
beschrieb Linux-Entwicklung mit IDE, Browser, Docker/VMs und drei externen
Monitoren ohne DisplayLink. Das ist bisheriger Planungskontext; Linux-Distribution
und konkretes Monitor-Setup sind noch nicht bestätigt.

## Quellen und Verknüpfungen

- [[2026-10-03--framework-notebook-konfiguration]] — bestätigte Bestellung
  und Gesprächsstand, ohne Kontakt- oder Zahlungsdaten.
- [[2026-10-03--framework-laptop-13-pro-intel-specs]] — datierter
  Herstellerabgleich mit Original-URLs.
- [[2026-10-03--framework-ssd-auswahl-und-preisabgleich]] — Größenpräferenz,
  recherchierte Kandidaten und datierter Preisabgleich.

## Offene Fragen und Widersprüche

- Welches SSD-Modell und Budget? 2 TB bevorzugt, 1 TB als Ausweichoption.
- Welche Linux-Distribution soll installiert werden?
- Welche drei Monitore mit welchen Auflösungen/Bildraten und welchem Dock
  sollen betrieben werden? Vier videofähige Slots belegen noch keine konkrete
  Drei-Monitor-Kompatibilität.
- Wann wird das Notebook tatsächlich versandt und geliefert?
- Die frühere persönliche Notiz favorisierte AMD mit DDR5 SO-DIMM.
  Die Bestellung bestätigt Intel mit LPCAMM2; die AMD-Empfehlung beschreibt
  nicht das bestellte Gerät.
- Frühere Intel-CPU-/iGPU-Angaben in der persönlichen Notiz weichen von den
  geprüften Herstellerdaten ab; maßgeblich für diesen Entwurf sind Bestellung
  und aktueller Herstellerabgleich.
