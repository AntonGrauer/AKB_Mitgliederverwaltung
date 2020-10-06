import pdftotext
import csv
import os

# Creating method in order to streamline subsequent assignments
def getValue (dataname, valueName):
    antragCleared = open("./Mitgliedsanträge/" + dataname, "r", encoding="utf-8")
    for line in antragCleared:
        lineValue = line.find(valueName)
        if lineValue != -1:
            lineValueCleared = line[lineValue+len(valueName)+1:]
            valueCleared = ''.join(lineValueCleared.split())
            return valueCleared

# Creating method in order to extract all information
def getInformation (fileName):
    categories = ("Vorname", "Nachname", "Telefon (mobil)", "E-Mail Adresse", "Geburtstag (Datum)",
                  "Straße", "PLZ", "Stadt", "Telefon (priv.)", "IBAN", "BIC", "Studiengang", "Eintrittssemester")
    allInformation = []
    for value in categories:
        allInformation.append(getValue(fileName, value))
    return allInformation

# Creating method that writes the whole data into a csv-file
def sendInformation(data):
    with open('Vorlage.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerows(data)

# Umsetzung der Methoden
antraegeDirectory = "./Mitgliedsanträge"
allFiles = os.listdir(antraegeDirectory)
allFiles.pop(0)
finalInformation = []
for antraege in allFiles:
    with open("./Mitgliedsanträge/" + antraege, "rb") as f:
        antragPDF = pdftotext.PDF(f)

    with open("./Mitgliedsanträge/" + antraege + '.txt', 'w') as f:
        f.write("\n\n".join(antragPDF))

    antragInformation = getInformation(antraege + '.txt')
    finalInformation.append(antragInformation)
    os.remove("./Mitgliedsanträge/" + antraege + '.txt')

sendInformation(finalInformation)