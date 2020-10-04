import pdftotext

# Load your PDF and save all text to a txt file
with open("Mitgliedsdaten.pdf", "rb") as f:
    antragPDF = pdftotext.PDF(f)

with open('Mitgliedsdaten.txt', 'w') as f:
    f.write("\n\n".join(antragPDF))

# Creating method in order to streamline subsequent assignments
def getValue (valueName):
    antragCleared = open("Mitgliedsdaten.txt", "r")
    firstName = 0
    for line in antragCleared:
        lineFirstName = line.find(valueName)
        if lineFirstName != -1:
            lineFirstNameCleared = line[lineFirstName+len(valueName)+1:]
            firstName = ''.join(lineFirstNameCleared.split())
    return firstName

# Creating method in order to extract all information
def getInformation ():
    information = list()
    categories = ("Vorname", "Nachname", "Telefon (mobil)", "E-Mail Adresse", "Geburtstag (Datum)",
                  "Straße", "PLZ", "Stadt", "Telefon (priv.)", "IBAN", "BIC", "Studiengang", "Eintrittssemester")
    for items in categories:
            information.append(getValue(items))
    return information

# Umsetzung der Methoden
allInformation = getInformation()
print (allInformation)


