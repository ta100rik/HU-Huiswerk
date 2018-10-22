import xmltodict
# declaring functions
def showcodenames(stations):
    print('Dit zijn de codes en types van de 4 stations')
    temp = '{:4}\t-\t{}'
    for station in stations:
        code = station['Code']
        type = station['Type']
        print(temp.format(code,type))
    print('')

def showmultisynoniem(stations):
    print('Dit zijn alle stations met één of meer synoniemen:')
    temp = '{:4}\t-\t{}'
    for station in stations:
        code = station['Code']
        syn = station['Synoniemen']
        if syn is not None:
            result = temp.format(code,syn)
            print(result)
    print('')

def longname(stations):
    print('Dit is de lange naam van elk station:')
    temp = '{:4}\t-\t{}'
    for station in stations:
        code = station['Code']
        name = station['Namen']['Lang']
        print(temp.format(code, name))
    print('')

# opening file and running functions
with open('Station.xml') as file:
    doc = xmltodict.parse(file.read())
    stations = doc['Stations']['Station']
    showcodenames(stations)
    showmultisynoniem(stations)
    longname(stations)

