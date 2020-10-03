import pdftotext

# Load your PDF
with open("Mitgliedsdaten.pdf", "rb") as f:
    antragPDF = pdftotext.PDF(f)

# Save all text to a txt file.
with open('Mitgliedsdaten.txt', 'w') as f:
    f.write("\n\n".join(antragPDF))

antragCleared = open("Mitgliedsdaten.txt", "r")

for line in antragCleared:
    lineFirstName = line.find('Vorname')
    if lineFirstName != -1:
        lineFirstNameCleared = line[lineFirstName+len('Vorname')+1:]
        firstName = ''.join(lineFirstNameCleared.split())
        print (firstName)