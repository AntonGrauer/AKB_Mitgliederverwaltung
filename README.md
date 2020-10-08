# AKB_Mitgliederverwaltung

pdfExtraction.py ist derzeit die Hauptdatei, die aus der Datei "Mitgliedsantrag.pdf" erst eine TXT-Datei erstellt ("Mitgliedsantrag.txt"),
anschließend daraus die relevanten Daten ausliest und in einer Liste speichert.
Diese Daten werden anschließend in der CSV-Datei ("Vorlage_BVH.csv") gespeichert.

Aufgabe: Implementierung des folgenden Prozesses - WICHTIG: Bei allen CSV-Dateien darf die erste Zeile nicht überschrieben werden

1. Befüllung der Datei "Vorlage_GSuite.csv"
  - Generierung einer Mail-Adresse für jedes Mitglied in der Form "nachname@akboerse.de"
        - Überprüfung, ob die Mailadresse bereits vorhanden ist (hierfür die Mitgliederliste nutzen)
        - wenn Adresse bereits vorhanden, Mailadresse ändern zu "[1.Buchstabe Vorname]nachname@akboerse.de"
        - Sofern auch diese Adresse schon verwendet wird, den 2. Buchstaben des Vornamens auch noch hinzunehmen
        - usw....
  - Befüllung der anderen relevanten Daten an Beispiel (Anton Grauer) orientieren
  - Für die Generierung eines Passworts müssen wir in Python acht Zufallszahlen & -buchstaben generieren und die dann eintragen

2. Befüllung der Datei "Vorlage Vorlage_BVH.csv"
  - Bei der Form an Beispiel (Anton Grauer) orientieren
  - Für Geschlecht prinzipiell "Herr" eintragen (das müssen wir im Nachgang dann korrigieren)
  - Semester ausgehend von Eintrittssemester in eine Zahl konvertieren (also aus HWS 20/21 eine 1 machen, aus FSS 21 eine 2, usw.)

3. Befüllung der Datei Vorlage_Website.csv
  - Bei der Form an Beispiel (Anton Grauer) orientieren
  - Überprüfung, ob der Nutzername bereits vorhanden ist (hierfür die Datei "ListeWebsite.csv" nutzen)
    - wenn Nutzername bereits vorhanden,  2. Buchstaben des Vornamens auch noch hinzunehmen
    - usw.
  - Für die ID die Mitgliedsnummer aus der Mitgliederliste nehmen
  
4. Befüllung der Datei Vorlage_Website.csv
  - Bei der Form an Beispiel (Anton Grauer) orientieren
  - Als Passwort das von Python generierte Passwort verwenden (muss zwingend übereinstimmen mit dem Passwort, welches wir in "Vorlage_GSuite.csv" schreiben

Zur Bearbeitung habe ich PyCharm mit Python 3.8 verwendet. Zudem werden die Packages pdftotext und csv benötigt.
