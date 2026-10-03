---
title: "Weitere einseitige Gen4-SSD-Alternativen für das Framework"
type: raw-research-report
tags: [research, framework, notebook, ssd]
origin: research-workflow
created: 2026-10-03
---

# Weitere einseitige Gen4-SSD-Alternativen für das Framework

## Conclusion

Zwei weitere Kandidaten für [[framework-notebook]] sind **KIOXIA EXCERIA
PLUS G3 2 TB** und **SK hynix Platinum P41 2 TB**. Beide Hersteller bestätigen
M.2 2280, einseitige Bestückung, PCIe 4.0 NVMe und TLC. Auch 1 TB wird geführt.
Ohne zusätzlichen Kühlkörper entsprechen sie Frameworks gefordertem
SSD-Format. Die Passung ist aus den Spezifikationen abgeleitet, nicht durch
einen direkten Test dieser Modelle im Intel-13-Pro bestätigt.

## Evidence

| Modell | Herstellerangaben | Einordnung |
| --- | --- | --- |
| KIOXIA EXCERIA PLUS G3 2 TB | TLC, HMB, einseitig; 80,15 × 22,15 × 2,63 mm; bis 5000/3900 MB/s | Mainstream-Alternative; nur bei attraktivem späterem Preis bevorzugen |
| SK hynix Platinum P41 2 TB | TLC, einseitig; Höhe max. 2,38 mm; bis 7000/6500 MB/s | Leistungsorientierte Alternative; kein belegter Effizienzvorsprung zur SN7100 |

KIOXIA nennt 5,3 W aktiv sowie 50/5 mW für PS3/PS4. Hersteller-Testwerte
sind nicht direkt mit anderen SSD-Testplattformen vergleichbar. SK hynix
bewirbt Effizienz, liefert auf der geprüften Produktseite jedoch keine
vergleichbare absolute Leistungsaufnahme. Maximalgeschwindigkeiten sagen
nichts über Dauerleistung nach dem SLC-Cache aus.

## Trade-offs and risks

- Weniger maximale Bandbreite macht die KIOXIA nicht automatisch sparsamer.
- KIOXIA **EXCERIA PLUS G3** nicht mit EXCERIA G3 ohne PLUS verwechseln;
  die Namen bezeichnen unterschiedliche Produkte.
- Für beide gibt es hier keine Messung im Framework, keine Zusage zu
  Linux-Suspend/Resume und keinen aktuellen Preis-/Lagervergleich.
- Die SN7100 bleibt aus der bisherigen Liste der Kandidat mit direktem
  Beleg aus dem passenden Framework-Konfigurator.

## Open questions

Später Preis, verfügbare genaue Ausführung, Firmware und vergleichbare
Notebook-Energiemessungen prüfen.

## Sources

Am 3. Oktober 2026 geöffnet; Produktseiten ohne klares Veröffentlichungsdatum.

- [KIOXIA – EXCERIA PLUS G3](https://europe.kioxia.com/en-europe/personal/ssd/exceria-plus-g3-nvme-ssd.html).
- [SK hynix – Platinum P41](https://ssd.skhynix.com/platinum_p41/).
- [Framework – Intel-Pro-SSD-FAQ](https://frame.work/products/laptop13pro-diy-intel-ultra-3/faq?faqable_id=274&faqable_type=section), im vorherigen Passungsabgleich geöffnet.
