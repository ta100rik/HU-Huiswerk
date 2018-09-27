file = open('Kaartnummers.txt','r')
for line in file:
    line = line.split(',')
    template = '{} heeft kaartnummer: {}'
    print(template.format(line[1].rstrip(),line[0]))
