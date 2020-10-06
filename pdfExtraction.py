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
            print (valueCleared)
            return valueCleared

# Creating method in order to extract all information
def getInformation (fileName):
    categories = ("Vorname", "Nachname", "Telefon (mobil)", "E-Mail Adresse", "Geburtstag (Datum)",
                  "Straße", "PLZ", "Stadt", "Telefon (priv.)", "IBAN", "BIC", "Studiengang", "Eintrittssemester")
    allInformation = []
    for value in categories:
        allInformation.append(getValue(fileName, value))
    return allInformation

def sendInformation(data):
    with open('Vorlage.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        street = []
        number = []
        for i in data:
            for r in range (0,len(i[5])-1,1):
                if i[5][r] in ("0","1","2","3","4","5","6","7","8","9"):
                    street = i[5][:r]
                    number = i[5][r:]
                    pass
        newstructure = [('',i[0],i[1],i[3],'1',street,number,i[6],i[7],i[11],i[12])]
        writer.writerows(newstructure)

# Umsetzung der Methoden
antraegeDirectory = "./Mitgliedsanträge"
allFiles = os.listdir(antraegeDirectory)
allFiles.pop(0)
for antraege in allFiles:
    with open("./Mitgliedsanträge/" + antraege, "rb") as f:
        antragPDF = pdftotext.PDF(f)

    with open("./Mitgliedsanträge/" + antraege + '.txt', 'w') as f:
        f.write("\n\n".join(antragPDF))

    antragInformation = getInformation(antraege + '.txt')
    os.remove("./Mitgliedsanträge/" + antraege + '.txt')

sendInformation(antragInformation)