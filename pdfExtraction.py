import pdftotext
import os

# Creating method in order to streamline subsequent assignments
def getValue (dataname, valueName):
    antragCleared = open("./Mitgliedsanträge/" + dataname, "r", encoding='latin1')
    firstName = 0
    for line in antragCleared:
        lineFirstName = line.find(valueName)
        if lineFirstName != -1:
            lineFirstNameCleared = line[lineFirstName+len(valueName)+1:]
            firstName = ''.join(lineFirstNameCleared.split())
    return firstName

# Creating method in order to extract all information
def getInformation ():
    categories = ("Vorname", "Nachname", "Telefon (mobil)", "E-Mail Adresse", "Geburtstag (Datum)",
                  "Straße", "PLZ", "Stadt", "Telefon (priv.)", "IBAN", "BIC", "Studiengang", "Eintrittssemester")
    antraegeDirectory = "./Mitgliedsanträge"
    allFiles = os.listdir(antraegeDirectory)
    allFiles.pop(0)
    rows, columns = (len(allFiles), len(categories))
    allInformation = [[0 for x in range(columns)] for x in range(rows)]
    for i in range(rows):
        with open("./Mitgliedsanträge/" + allFiles[i], "rb") as f:
            antragPDF = pdftotext.PDF(f)

        with open("./Mitgliedsanträge/" + allFiles[i] + '.txt', 'w') as f:
            f.write("\n\n".join(antragPDF))

        for j in range(columns):
            print (getValue("Mitgliedsdaten Kopie.pdf.txt", categories[1]))
            allInformation[i][j] = getValue(allFiles[i], categories[j])
    return allInformation

# Umsetzung der Methoden
finalInformation = getInformation()
print (finalInformation)



