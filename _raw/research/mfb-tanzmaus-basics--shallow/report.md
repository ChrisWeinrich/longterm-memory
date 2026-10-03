---
title: "MFB Tanzmaus: Einstieg und Video-Empfehlung"
type: raw-research-report
tags: [research, music, drum-machine, mfb-tanzmaus]
origin: research-workflow
created: 2026-09-13
---

# MFB Tanzmaus: Einstieg und Video-Empfehlung

## Conclusion

Für den Wiedereinstieg ist das Video **MFB Tanzmaus Interface Guide** von
once upon a synth der bessere erste Schritt als die vollständige Anleitung.
Die Tanzmaus verwendet kontextabhängige Mehrfachbelegungen; das Video erklärt
die Bedienlogik in Reihenfolge und deckt die wichtigsten Grundlagen in knapp
20 Minuten ab.

Minimaler Startpfad:

1. Netzteil, Master-Out und Abhöre anschließen; Tanzmaus vor der Abhöre
   einschalten.
2. Im Play-Mode ein Werks-Pattern aus Bank 1 wählen und Start/Stop bedienen.
3. Einen Track muten, dann Bassdrum, Snare und Clap mit den Reglern verändern.
4. Erst danach ein leeres Pattern in Bank 2–4 im Step-Record bauen.
5. Nach einem gelungenen Pattern sofort speichern; vor MIDI-Dumps Sicherungen
   anlegen, da ein eingehender Bank-Dump die aktuelle Bank ohne Undo ersetzt.

Video-Reihenfolge: 00:09 Übersicht, 02:40 Modi, 03:06 Step-Recording,
14:03 Play-Mode, 14:25 Patterns/Bänke, 17:21 Speichern. Alles andere kann
vorerst warten.

## Evidence

- Das offizielle Handbuch beschreibt drei zentrale Betriebsarten: Play,
  Manual Trigger und Record. Die Step-Taster wechseln ihre Bedeutung nach
  Betriebsart; Shift erschließt Direkt- oder mehrstufige Zweitfunktionen.
- Es gibt 64 Patterns: vier Bänke mit je 16 Patterns. Bank 1 enthält
  Werks-Patterns; Bänke 2–4 sind leer.
- Der Videoguide behandelt genau die Einsteigerabfolge inklusive Modes,
  Step-Recording, Play-Mode, Patterns/Bänke und Speichern.

## Trade-offs and risks

- Das Video ist englisch und von 2017, bleibt aber passend zum unveränderten
  Hardware-Workflow.
- Keine großen Lautstärken beim ersten Start. Handbuch: Tanzmaus zuerst,
  danach Audiosystem.
- Einzelausgänge nehmen den jeweiligen Sound aus dem Master-Out heraus.
- Bank-Empfang per MIDI-SysEx überschreibt die aktuelle Bank ohne Undo.

## Open questions

- Ist die Tanzmaus allein am Mixer/Interface oder soll sie zu einer DAW bzw.
  einem anderen MIDI-Clock-Geber synchron laufen? Das bestimmt den sinnvollen
  nächsten Mini-Guide.

## Sources

- Official German manual (hosted by Thomann), accessed 2026-09-13:
  https://images.thomann.de/pics/atg/atgdata/document/manual/tanzmaus_dt.pdf
- once upon a synth, *MFB Tanzmaus Interface Guide* (2017), video identifier
  and chapter list verified via Matrixsynth, accessed 2026-09-13:
  https://www.youtube.com/watch?v=SEmE_-isRGM
- Matrixsynth mirror of the guide description and chapter list, accessed
  2026-09-13: https://www.matrixsynth.com/2017_01_02_archive.html
