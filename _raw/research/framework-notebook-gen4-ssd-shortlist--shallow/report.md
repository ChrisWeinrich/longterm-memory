---
title: "Framework Notebook: Gen4-SSD-Auswahl mit 2 TB und 1 TB"
type: raw-research-report
tags: [research, framework, notebook, ssd, hardware]
origin: research-workflow
created: 2026-10-03
---

# Framework Notebook: Gen4-SSD-Auswahl mit 2 TB und 1 TB

## Conclusion

Für [[framework-notebook]] zuerst **WD_BLACK/Sandisk SN7100 2 TB** und
**Samsung 990 EVO Plus 2 TB** vergleichen. **Lexar NM790 2 TB ohne Kühlkörper**
ist ein weiterer Kandidat. **Samsung 990 PRO 2 TB ohne Kühlkörper** ergänzt
die Liste als TLC-Modell mit eigenem DRAM für anspruchsvollere gemischte I/O.

Das ist eine Auswahl nach technischen Eigenschaften und Notebook-Ausrichtung,
keine gemessene Temperatur-/Effizienz-Rangfolge. Grundlage ist
[[framework-notebook-ssd-type--shallow/report|die vorherige Typrecherche]].
Keine aktuellen Preise oder Händlerverfügbarkeiten recherchiert.

2 TB ist als Planungsziel für Entwicklungsumgebungen, Container und VM-Images
vernünftig. 1 TB ist eine Ausweichoption bei geringerem lokalen Datenbestand
oder begrenztem Budget. Das ist eine Bedarfseinschätzung, keine bestätigte
Kapazitätsanforderung. Alle vier Familien führen 1- und 2-TB-Varianten.

## Evidence

Alle Kandidaten sind M.2 2280 NVMe mit Gen4-x4-Unterstützung.
Geschwindigkeiten sind beworbene Maximalwerte für 2 TB, keine Dauerwerte.

| Kandidat, jeweils 2 TB | NAND / Cache | Lesen / Schreiben bis | Einordnung für das Notebook |
| --- | --- | --- | --- |
| WD_BLACK/Sandisk SN7100 | TLC, DRAMlos | 7250 / 6900 MB/s | Hersteller richtet das Design ausdrücklich auf Notebooks/Handhelds und Effizienz aus; erster Kandidat [1] |
| Samsung 990 EVO Plus | TLC, HMB | 7250 / 6300 MB/s | Gut dokumentierte Leistungsaufnahme und Stromsparzustände; ebenfalls erste Auswahl [2] |
| Lexar NM790, ohne Kühlkörper | TLC-Familie, HMB | 7400 / 6500 MB/s | Effizienzorientierte Alternative; Herstellervergleich ohne direkt vergleichbare absolute Wattwerte [3][4] |
| Samsung 990 PRO, ohne Kühlkörper | TLC, 2 GB eigener LPDDR4-DRAM | 7450 / 6900 MB/s | Alternative bei anspruchsvoller VM-/DB-I/O; Mehrwert und Energiebedarf konkret abwägen [5] |

### Energie und Thermik

Samsung nennt für die 990 EVO Plus 2 TB durchschnittlich 4,6 W Lesen und
4,2 W Schreiben sowie 60 mW in PS3 und 5 mW in PS4/L1.2. Für die 990 PRO
2 TB stehen 6,1/5,5 W, 55 mW Idle mit APST und 5,8 mW in L1.2 im Datenblatt.
Die Desktop-Testplattformen unterscheiden sich. Das sind Herstellerangaben,
kein direkter Benchmark und keine Linux-/Framework-Verbrauchszusage. [2][5]

Sandisks Effizienzverbesserung bezieht sich auf den Vergleich mit der SN770
1 TB bei maximaler Geschwindigkeit, nicht auf eine garantierte Akkuverbesserung
gegenüber der übrigen Auswahl. Lexars bis zu 40 Prozent beziehen sich auf
interne Vergleiche mit DRAM-bestückten Gen4-SSDs; die geprüfte Seite nennt
keinen ausreichend transparenten gemeinsamen Test für diese Auswahl. [1][3]

**Ableitung:** SN7100 und EVO Plus sind passende Ausgangspunkte für die
gewünschte effiziente TLC-Klasse. Eine sichere Aussage „Modell X ist am
kühlsten“ lässt sich daraus nicht machen. Eigener DRAM allein garantiert
auch keine bessere Dauerleistung.

## Trade-offs and risks

- Samsung vermarktet die EVO Plus auch als Gen5 x2. Sie unterstützt ausdrücklich
  Gen4 x4 und gehört deshalb in diese Auswahl; kein Gen5-x4-Spitzenmodell. [2]
- 1 TB bietet weniger Platzreserve. Bei EVO Plus sind zudem 7150 statt 7250 MB/s
  Lesen angegeben; daraus folgt kein bedeutender Alltagsnachteil. [2]
- Für NM790 belegt die geöffnete Bare-Drive-Seite HMB und Abmessungen, die
  geöffnete Heatsink-Familienseite TLC. Die exakte Bare-Drive-Artikelrevision
  vor Kauf bestätigen. Ein ergänzendes Lexar-PDF war nicht abrufbar und wird
  nicht als verifizierte Quelle für einseitige Bestückung verwendet.
- Einseitige Bestückung der exakten 2-TB-SKUs und Einbauhöhe vor Kauf prüfen;
  dünne Abmessungen allein beweisen keine einseitige Bestückung.
- Keine Daten zu thermischer Drosselung oder Leistung nach dem SLC-Cache aus
  vergleichbaren Messungen erhoben. Hersteller-Maximalwerte reichen hierfür nicht.
- Firmware-Update-Pfad unter Linux prüfen. Sandisk nennt seinen Dashboard-
  Updater ausdrücklich als Windows-only. [1]
- Crucial T500 wurde als zusätzlicher Kandidat gesucht, das offizielle
  Datenblatt ließ sich nicht abrufen. Deshalb hier nicht detailliert bewertet.

## Open questions

- Späterer Preisvergleich zwischen den drei bevorzugten 2-TB-Kandidaten und
  ihren 1-TB-Versionen; noch außerhalb des Umfangs.
- Vergleichbare Tests für Idle, aktive Energie, Temperaturen und Cache-Ende.
- Linux-Suspend/Resume und aktueller Firmwarestand der endgültigen SKU.
- Wie viel Platz brauchen vorhandene Repositories, Container und VMs tatsächlich?

## Sources

Am 3. Oktober 2026 gesucht und geöffnet; Produktseiten ohne eindeutiges
Veröffentlichungsdatum. Nur Herstellerquellen für technische Angaben verwendet.

1. [Sandisk – WD_BLACK SN7100](https://www.sandisk.com/products/ssd/internal-ssd/wd-black-sn7100-nvme-internal-ssd).
   TLC, Kapazitätsvarianten, Leistung und Notebook-Ausrichtung.
2. [Samsung – 990 EVO Plus Datenblatt Revision 1.0](https://download.semiconductor.samsung.com/resources/data-sheet/samsung_nvme_ssd_990_evo_plus_datasheet_rev.1.0_10139908980019.pdf).
   Oktober 2024; Kapazitäten, TLC/HMB, Leistungsaufnahme und Testbedingungen.
3. [Lexar – NM790 ohne Kühlkörper](https://americas.lexar.com/product/lexar-nm790-m-2-2280-pcie-gen-4x4-nvme-ssd/).
   HMB, Kapazitäten, Leistung und Hersteller-Effizienzvergleich.
4. [Lexar – NM790-Familie mit Kühlkörper](https://www.lexar.com/es/products/NM790-with-Heatsink-M-2-2280-PCIe-Gen-4x4-NVMe-SSD/).
   Explizite TLC-Angabe; die Kühlkörpervariante ist nicht die Kaufempfehlung.
5. [Samsung – 990 PRO Datenblatt Revision 2.0](https://download.semiconductor.samsung.com/resources/data-sheet/samsung_nvme_ssd_990_pro_datasheet_rev.2.0.pdf).
   Juli 2023; TLC/DRAM, Leistungsaufnahme und Testbedingungen.
