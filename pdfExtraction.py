import pdftotext

# Load your PDF and save all text to a txt file
with open("Mitgliedsdaten.pdf", "rb") as f:
    antragPDF = pdftotext.PDF(f)

with open('Mitgliedsdaten.txt', 'w') as f:
    f.write("\n\n".join(antragPDF))

antragCleared = open("Mitgliedsdaten.txt", "r")

# Creating method in order to streamline subsequent assignments
def getValue (valueName, antrag):
    firstName = 0
    for line in antrag:
        lineFirstName = line.find(valueName)
        if lineFirstName != -1:
            lineFirstNameCleared = line[lineFirstName+len(valueName)+1:]
            firstName = ''.join(lineFirstNameCleared.split())
    return firstName

vorname = getValue("Vorname", antragCleared)
print (vorname)

categories = ("Vorname", "Nachname", "Telefon (mobil)", "E-Mail Adresse", "Geburtstag (Datum)",
              "Straße", "PLZ", "Stadt", "Telefon (priv.)", "IBAN", "BIC", "Studiengang", "Eintrittssemester")

allInformation = list()

for var in categories:
        allInformation.append(getValue(var, antragCleared))

print (allInformation)


