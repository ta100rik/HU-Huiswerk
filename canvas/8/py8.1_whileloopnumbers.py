bol = True
list = []

while bol:
    Number = int(input('Geef een getal:'))
    if Number == 0:
        template = 'Er zijn {} getallen ingevoerd, de som is: {}'
        print(template.format(len(list),sum(list)))
        bol = False
    else:
        list.append(Number)

