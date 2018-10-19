def inlezen_beginstation(stations):
    bol = True
    while bol:
        askstation = input('What station do you start? ')
        for station in stations:
            if askstation == station:
                return station
                bol = False


def inlezen_eindstation(stations, beginstation):
    while True:
        askstation = input('What station do you end? ')
        for station in stations:
            if askstation == station:
                beginindex = stations.index(beginstation)
                endindex = stations.index(askstation)
                if beginindex < endindex:
                    return station
                else:
                    print('dit station is de trein al langs geweest geef een ander station op')

def omroepen_reis(stations, beginstation, eindstation):
    indexbegin = stations.index(beginstation) + 1
    indexend = stations.index(eindstation) + 1
    tussen = indexend - indexbegin
    prijs = tussen * 5
    beginstationtemp = 'Het beginstation {} is het {}e station in het traject.'
    eindstationtemp = 'Het eindstation {} is het {}e station in het traject'
    afstand = 'De afstand bedraagt {} stations'
    prijstemp = 'De prijs van het kaartje is {} euro'
    begintemp = 'Jij stapt in de trein in: {}'
    eindtemp = 'Jij stapt uit de trein in: {}'
    print(beginstationtemp.format(str(beginstation),str(indexbegin)))
    print(beginstationtemp.format(str(eindstation),str(indexend)))
    print(afstand.format(str(tussen)))
    print(prijstemp.format(str(prijs)))
    print(begintemp.format(beginstation))
    for staitionindex in range(stations.index(beginstation) + 1,stations.index(eindstation)):
        print(' -' + stations[staitionindex])
    print(eindtemp.format(eindstation))

stations = [
    'Schagen',
    'Heerhugowaard',
    'Alkmaar',
    'Castricum',
    'Zaandam',
    'Amsterdam Sloterdijk',
    'Amsterdam Centraal',
    'Amsterdam Amstel',
    'Utrecht Centraal',
    '’s-Hertogenbosch',
    'Eindhoven',
    'Weert',
    'Roermond',
    'Sittard',  
    'Maastricht'
    ]
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)