# TGOE-Coding_Task_2

## Aufgabe:

Implementieren Sie eine Funktion MERGE die eine Liste von Intervallen entgegennimmt und als Ergebnis wiederum eine Liste von Intervallen zurückgibt. Im Ergebnis sollen alle sich überlappenden Intervalle gemerged sein. Alle nicht überlappenden Intervalle bleiben unberührt.

Beispiel:
Input: [25,30] [2,19] [14, 23] [4,8]  Output: [2,23] [25,30]

### Vorgehen:

* Sortieren der Liste mit den Intervallen:
  [25,30] [2,19] [14, 23] [4,8]  => [[2, 19], [4, 8], [14, 23], [25, 30]]
* Solange die obere Grenze des ersten Intervalls größer ist als die untere Grenze des zweiten Intervalls, findet eine Überlappung statt. Bspl.: 19 > 4
* Sobald keine Überlapung stattfindet wird das Intervall in eine Liste gespeichert. 

### Lösung:
Code/Loesung.py

## Wie ist die Laufzeit Ihres Programms ?

```
$ cd ../Loesung.py
$ time Loesung.py

real	0m0.002s
```
Die Laufzeit beträgt 200ms


## Wie kann die Robustheit sichergestellt werden, vor allem auch mit Hinblick auf sehr große Eingaben?

Durch das Abfangen von fehlerhaften Eingaben oder Datentypen kann die Robustheit der Software verbessert werden,
eine Prüfung auf eine leere Liste ist beispielsweiße implementiert.
Zusätzlich könnten sehr große Intervalle durch vorheriges überprüfen abgelehnt werden.

## Wie verhält sich der Speicherverbrauch ihres Programms?
Der Datenspeicher wird vom Skript nicht verwendet und der Arbeitsspeicherverbrauch wird durch eine Beschränkung auf die notwendigen Variablen und Funktionen sichergestellt. 



