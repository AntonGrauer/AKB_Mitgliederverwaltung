# AKB_Mitgliederverwaltung

Prozess Neuantrag:
Antragsstellung
1. Auf Website ist Antrag verlinkt —> Öffnung neuer Tab mit Mitgliedsantrag (provided by easyVerein)
2. Sobald ausgefüllt: Mail mit PDF an IT-Department gesendet & Hinterlegung in EasyVerein zur Genehmigung

Bearbeitung der Daten:
1. Genehmigung der Mitglieder in EasyVerein
2. Speichern der PDF in lokalem PC-Ordner
3. Auslesen der Daten und Befüllung mehrere CSV-Dateien
    1. Excel-Mitgliederliste befüllen (Annahme: Aktuelle Liste ist im gleichen Directory wie Code abgelegt)
        - Neue Daten in erste Leere Zeile schreiben 
            - Generierung AKB-Mail und checken, ob diese schon in Mitgliederliste vorkommt
            - Generierung Neue Mitgliedsnummer (fortlaufend)
            - Hinterlegung AKB-Mail und Mitgliedsnummer in ‘data’ (‘data’ weiterhin Referenz für Befüllung anderer CSV-Dateien)
    2. G-Suite (in erste Zeile müssen Spaltenüberschriften geschrieben werden (siehe Vorlage_GSuite))
        - Generierung Passwort
        - Nutzung AKB-Mailadresse
    3. BVH: Portal für Zeitschriftenverwaltung (in erste Zeile Spaltenüberschriften (siehe Vorlage BVH))
        - Feld Adresszusatz nicht befüllen, alles nach dem Straßennamen in Spalte Hausnummer schreiben
    4. Mailchimp: Mailportal (in erste Zeile Spaltenüberschriften (siehe Vorlage Mailchimp))
        - Achtung: Mailadressen nicht vertauschen (in vorderer Spalte steht private Mailadresse)
    5. Wordpress: Website-Benutzer (in erste Zeile Spaltenüberschriften (siehe Vorlage BVH))
        - Für Spalte ID Mitgliedsnummer nehmen

Upload
1. Hochladen der CSV-Dateien in die Portale
2. Aktualisierung der AKB-Mailadressen in EasyVerein
3. Versenden einer Automatisierten Mail in Mailchimp mit Mitgliedsdaten

Weiteres Vorgehen Projekt:
1. Befüllung der CSV-Dateien (muss reibungsfrei laufen!!!!)
2. Automatisierung des Uploads (mit G-Suite anfangen und danach kontinuierlich ausbauen)
3. Integrierung in Website etc.



Zur Bearbeitung habe ich PyCharm mit Python 3.8 verwendet. Zudem habe ich das Package pdftotext installiert.
