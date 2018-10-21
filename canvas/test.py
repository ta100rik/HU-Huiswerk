bestand=open('kaartnummers.txt', 'r')
data = bestand.read()
numberOfLines = len(data.splitlines())
print('Deze file telt '+str(numberOfLines)+' regels')
list = data.splitlines()
kaartnummer = []
for item in list:
    item = item.split(',')
    kaartnummer.append(item[0])
maximalekaartnummer = max(kaartnummer)
indexmax = kaartnummer.index(max(kaartnummer)) + 1