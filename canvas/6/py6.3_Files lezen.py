file = open('Kaartnummers.txt','r')
linecount = 1
for line in file:
    max = 0
    line = line.split(',')
    if int(line[0]) > max:
        max = line[0]
        singlelist = [linecount,max]#putting linenumber and value in 1 list
    linecount += 1
template = 'Deze file telt {} regels \nHet grootste kaartnummer is: {} en dat staat op regel {}'
print(template.format(linecount,singlelist[1],singlelist[0]))
