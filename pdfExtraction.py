import pdftotext

# Load your PDF
with open("Mitgliedsdaten.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)
    print (pdf)

# Save all text to a txt file.
with open('Mitgliedsdaten.txt', 'w') as f:
    f.write("\n\n".join(pdf))

file = open("Mitgliedsdaten.txt", "r")
print (file.read())