import xmltodict

with open('Stock.xml') as file:
    doc = xmltodict.parse(file.read())
    for artikel in doc['artikelen']['artikel']:
        print(artikel['naam'])