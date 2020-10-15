import csv
import os
import random
import string
import pandas
import pdftotext


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
                  "Straße", "Hausnummer", "PLZ", "Stadt", "Telefon (priv.)", "Straße (gesch.)",
                  "PLZ (gesch.)", "Stadt (gesch.)", "IBAN", "BIC", "Studiengang", "Eintrittssemester")
    allInformation = []
    for value in categories:
        allInformation.append(getValue(fileName, value))
    return allInformation

# creating method to create email address
def createMail( prename, surname):
    with open('Vorlage_GSuite.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        gsuitemails = list(reader)
    maillist = []
    for i in gsuitemails:
        maillist = maillist+(i)
    mail = surname + "@akboerse.de"
    prename.replace(" ","")
    a = 0
    while mail in maillist: #to prevent addresses from being handed to more than one person
        mail = mail[:a]+ prename[a] + mail[a:]
        a += 1
    return mail

#method to generate passkeys
def createPasskey():
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join((random.choice(letters_and_digits) for i in range(8)))

# Creating method that writes data into every database
def sendInformation(data):
    with open('Vorlage_BVH.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerows(data)
    with open('Vorlage_GSuite.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        for i in range(0, len(data)):  # data gets formated so it only contains necessary information
            writer.writerows([[data[i][0], data[i][1], createMail(data[i][0], data[i][1]), createPasskey(), "", "/Normale Mitglieder", "",
                 data[i][3]]])


# Umsetzung der Methoden
def start():
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
        print (antragInformation)
        finalInformation.append(antragInformation)
        os.remove("./Mitgliedsanträge/" + antraege + '.txt')

    sendInformation(finalInformation)
start()
