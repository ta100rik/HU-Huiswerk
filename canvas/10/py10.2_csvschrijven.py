import datetime
import csv
bestand = 'inlog.csv'

while True:
    now = datetime.datetime.now()
    now = now.strftime("%a %d %b %Y at %H:%M")
    naam = input("Wat is je achternaam? ")
    voorl = input("Wat zijn je voorletters? ")
    gbdatum = input("Wat is je geboortedatum? ")
    email = input("Wat is je e-mail adres? ")
    with open(bestand, 'a') as newFile:
        newFileWriter = csv.writer(newFile, delimiter=';')
        newFileWriter.writerow([now,naam,voorl,gbdatum,email])
