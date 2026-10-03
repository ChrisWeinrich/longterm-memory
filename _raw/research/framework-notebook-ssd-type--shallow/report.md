---
title: "SSD-Typ für Framework Laptop 13 Pro: Leistung, Kostenklasse und Energie"
type: raw-research-report
tags: [research, framework, notebook, ssd, hardware, energy]
origin: research-workflow
created: 2026-10-03
---

# SSD-Typ für Framework Laptop 13 Pro: Leistung, Kostenklasse und Energie

## Conclusion

**Empfohlener Ausgangspunkt: M.2 2280 NVMe, PCIe 4.0 x4, 3D-TLC-NAND,
einseitig bestückt, ohne aufgesetzten Kühlkörper; effiziente Client-Klasse.
Eine gute DRAMlose Ausführung mit HMB ist geeignet.**

Dies ist eine abgeleitete Empfehlung für Christians Framework Laptop 13 Pro
DIY mit Intel Core Ultra X7 358H und 32 GB LPCAMM2, siehe
[[framework-notebook]]. Als Workload wird der bisherige Planungskontext
Linux, IDE, Browser und gelegentliche Docker-/VM-Nutzung angenommen.
Schwere dauerhafte VM-/Datenbank-I/O ist nicht bestätigt.

PCIe 5.0 bleibt eine sinnvolle Alternative, wenn die konkrete SSD unter
vergleichbarer Last mindestens ebenso effizient ist und ihre Mehrleistung
gebraucht wird. Gen5 ist weder automatisch zu heiß noch automatisch besser.
Die vorhandene Gen5-Unterstützung verpflichtet nicht zum Kauf einer Gen5-SSD.

Umfang: Typ und qualitative Kosten-/Nutzenabwägung. Keine Angebote,
aktuellen Preise, Hersteller-Rangliste oder Kapazitätsentscheidung.

## Evidence

### Physische und elektrische Passung

Framework bestätigt M.2 2280 NVMe und bietet für das Intel-Pro-Modell sowohl
Gen4 als auch Gen5 an. Doppelseitige SSDs erfordern laut Einbauanleitung eine
Anpassung am Mainboard-Thermalpad; Heatspreader sind zu entfernen oder zu
vermeiden. Einseitig ohne aufgesetzten Kühlkörper vereinfacht daher die
Passung. Das ist eine mechanische Präferenz, keine Garantie für geringere
Temperaturen. [1][2]

### TLC oder QLC?

TLC speichert drei, QLC vier Bits pro Zelle. QLC bietet höhere Dichte und
potenziell geringere Kosten pro Kapazität; TLC ist die ausgewogene Klasse
für Leistung und Schreibhaltbarkeit. QLC ist besonders für überwiegend
lesende Nutzung interessant. Das sind NAND-Tendenzen, keine absoluten
Leistungsgrenzen fertiger SSDs. [3]

**Ableitung:** Für ein einziges Systemlaufwerk mit Entwicklungsdateien,
Containern und VM-Images ist TLC die konservative Wahl. QLC ist vertretbar,
wenn Kapazität/Kosten Vorrang haben und lange Schreiblasten selten sind.
Ohne Preise wird kein aktueller Preisvorteil behauptet.

### DRAM, HMB und SLC-Cache auseinanderhalten

HMB erlaubt DRAMlosen SSDs die Nutzung eines Teils des Host-RAMs. Offizielle
Client-Produkte zeigen, dass TLC + HMB eine etablierte Notebook-Klasse ist.
Eigener SSD-DRAM ist deshalb keine zwingende Voraussetzung. [3][4]

DRAM/HMB dienen insbesondere der Verwaltung von Adresszuordnungen;
der SLC-Schreibcache ist ein anderer Mechanismus im NAND. Auch TLC-SSDs
können nach dessen Erschöpfung langsamer schreiben. Eine Forschungsarbeit
beschreibt Cache-Sättigung und zusätzliche interne Schreibarbeit bei der
Cache-Räumung. Sie liefert keine Rangliste aktueller Kaufprodukte. [5]

**Ableitung:** Bei gelegentlichen Builds und Containern HMB akzeptieren.
Bei vielen gleichzeitig aktiven VMs, Datenbanken oder langen Schreibläufen
eine TLC-Ausführung mit eigenem DRAM stärker gewichten. DRAM allein
garantiert weder Dauerleistung noch niedrigen Verbrauch; Messungen bleiben nötig.

### Wärme und Energie: Messzustand zählt

NVMe unterscheidet aktive und stromsparende Zustände. APST, PCIe-Link-
Stromsparzustände und Runtime D3 können den Leerlaufverbrauch stark senken;
die Umsetzung hängt auch von Host, Betriebssystem und Firmware ab. [6]

Ein offizielles TLC/HMB-Datenblatt nennt exemplarisch mehrere Watt bei
aktiven Transfers und wenige Milliwatt im tiefen Stromsparzustand. Diese
Werte sind modell- und testabhängig, keine Zusage für das Framework unter
Linux. Active Idle und tiefer Sleep dürfen nicht gleichgesetzt werden. [4]

Microns eigener Vergleich zeigt eine neuere Gen5-QLC-SSD mit niedrigerer
Active-Idle-Aufnahme als die verglichenen Gen4- und Gen5-TLC-Produkte.
Das widerlegt eine starre Rangfolge nach PCIe-Generation oder NAND-Typ,
beweist aber keine allgemeine Überlegenheit. Hersteller-Labortest, keine
unabhängige Messung am Framework. [7]

**Ableitung:** Für Akkubetrieb zählen Idle/Sleep und Energie pro erledigter
Aufgabe; für lange Transfers aktive Leistungsaufnahme und Drosselung.
Ein schnelleres Laufwerk kann früher schlafen. Niedrigere Spitzenleistung
allein bedeutet daher nicht weniger Gesamtenergie.

## Trade-offs and risks

Die Tabelle ist eine qualitative Einordnung, keine gemessene Produktwertung.
Kosten beziehen sich auf die Auslegung, nicht auf aktuelle Marktpreise.

| Klasse | Kosten-/Leistungsprofil | Wärme/Energie und Passung |
| --- | --- | --- |
| Gen4 TLC, effizientes HMB-Design | Ausgewogene Ausgangswahl für normale Entwicklung | Gute Notebook-Klasse; Idle und Dauerlast später konkret prüfen |
| Gen4 TLC mit eigenem DRAM | Mehr Reserve bei anspruchsvoller gemischter I/O möglich; zusätzliche Komponente | Für intensive VM-/DB-Nutzung erwägen; nicht automatisch heißer oder sparsamer |
| Gen4/Gen5 QLC | Dichte/Kosten im Vordergrund; Cache und Schreibhaltbarkeit besonders prüfen | Kann sehr effizient sein; für lange Schreiblasten weniger konservative Wahl |
| Gen5 TLC, effiziente Client-Klasse | Höhere sequenzielle Bandbreite; Mehrwert workloadabhängig | Geeignet bei guten Effizienzmessungen, kein pauschaler Ausschluss |
| Gen5 auf maximale Dauerleistung ausgelegt | Leistungsreserve für große Transfers; Aufwand eventuell ohne Alltagsnutzen | Thermisches Budget kritisch prüfen; aufgesetzter Kühlkörper passt nicht zum empfohlenen Einbauprofil |

Für interaktive Entwicklung lässt sich aus maximaler sequenzieller
Bandbreite kein proportionaler Zeitgewinn ableiten. Kleine Zugriffe bei
niedriger Queue Depth, gemischte Last und Schreibleistung nach dem SLC-Cache
sind für die spätere Auswahl aussagekräftiger. Das ist eine Workload-Ableitung,
kein gemessener Build-Benchmark.

## Open questions

- Wie intensiv sind lokale VMs, Datenbanken und große Schreibvorgänge?
- Welche Kapazität wird benötigt? Bestückung, Cache und Verbrauch können
  zwischen Kapazitätsvarianten derselben Familie variieren.
- Bei späterer Modellauswahl prüfen: Linux-Suspend/Resume, APST/ASPM,
  Idle-Verbrauch, Dauerleistung nach Cache, thermische Drosselung und Firmware.
- Ohne konkrete Produkte und Tests ist keine belastbare Watt-, Temperatur-
  oder Akkulaufzeit-Rangfolge möglich. Typempfehlung bleibt Vorfilter.
- Die Notebook-Seite ist noch ein Wiki-Entwurf; der Raw-Bericht ist ebenfalls
  nicht akzeptiertes Wissen.

## Sources

Alle URLs am 3. Oktober 2026 geöffnet. Herstellerdaten dienen als technische
Primärquellen, nicht als Kaufempfehlung für die genannten Marken.

1. [Framework Laptop 13 Pro – Spezifikationen](https://frame.work/laptop13pro?tab=specs).
   Bereits im Gespräch geöffnet; Intel-Variante, Gen4-/Gen5-Optionen.
2. [Framework – SSD-Austauschanleitung](https://guides.frame.work/Guide/Storage-%2BSSD%2BReplacement%2Bfor%2BFramework%2BLaptop%2B13%2BPro/763).
   Bereits im Gespräch geöffnet; Bauform und mechanische Einbauhinweise.
3. [KIOXIA – Flash Memory Matters: Understanding Your SSD Options](https://blog-us.kioxia.com/post/2025/04/25/flash-memory-matters-understanding-your-ssd-options).
   25. April 2025; TLC/QLC-Abwägung und HMB-Client-Klasse.
4. [Samsung – 990 EVO Datenblatt, Revision 1.1](https://download.semiconductor.samsung.com/resources/data-sheet/samsung_nvme_ssd_990_evo_datasheet_rev.1.1.pdf).
   Dokumentjahr 2024; TLC/HMB und getrennte aktive/Idle-Leistungsangaben.
5. [In-place Switch: Reprogramming based SLC Cache Design for Hybrid 3D SSDs](https://arxiv.org/abs/2409.14360).
   2024, Forschungs-Preprint; Cache-Sättigung und interne Schreibarbeit.
6. [NVM Express – Technology Power Features](https://nvmexpress.org/resource/technology-power-features/).
   Standardsorganisation; aktive/nichtoperative Zustände, APST und Runtime D3.
7. [Micron – Power efficiency enables AI-era client performance](https://www.micron.com/about/blog/storage/ssd/power-efficiency-enables-ai-era-client-performance).
   Hersteller-Labortest; datiert nicht eindeutig ausgewiesen, beschreibt 2026er
   Plattform. Beleg für modellabhängige Effizienz statt pauschaler Gen4/Gen5-Rangfolge.
