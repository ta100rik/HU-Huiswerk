import csv
import os.path
print('Welcome this is a csv reader / maker\n')
filename = input('What is the filename: ')
while True:
    action = input('What do you want to do?\n1. New file\n2. Read file(assingment specific)\n3. Wrong file, choose another 1\n4. Quit this program\nPlease provide action number: ')
    if action == '1':
        if os.path.isfile(filename):
            print('This file is already existing....\nRerunning program')
            filename = input('What is the filename: ')
        else:
            headers = []
            lines = []
            while True:
                header = input('Type in your headers you want say \'break\' if you done with the headers: ')
                if header == 'break':
                    break
                else:
                    headers.append(header)
            while True:
                bol = input('Do you want to add a new line? (yes(Y) or no (N))')
                if bol == 'Y':
                    line = []
                    for head in headers:
                        headinput = input('Insert {} : '.format(head))
                        line.append(headinput)
                    lines.append(line)
                    print('line added')
                elif bol == 'N':
                    with open(filename, 'w') as csvfile:
                        filewriter = csv.writer(csvfile, delimiter=',',escapechar=' ',lineterminator='\n')
                        filewriter.writerow(headers)
                        for line in lines:
                            filewriter.writerow(line)
                        break
    elif action == '2':
        if os.path.isfile(filename):
            with open(filename) as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                highestpriceproduct = []
                lowestproduct = []
                totalproducts = 0
                highestprice = 0
                loweststock = 0
                rowcount = 0
                for row in readCSV:
                    if rowcount >= 1:
                        artikelnummer = row[0]
                        artikelcode = row[1]
                        naam = row[2]
                        voorraad = int(row[3])
                        prijs = float(row[4])
                        totalproducts = 1 + totalproducts
                        if highestprice < prijs:
                            highestprice = prijs
                            highestpriceproduct = row
                        if loweststock < voorraad:
                            loweststock = voorraad
                            lowestproduct = row
                    rowcount = 1 + rowcount
                temp1 = 'Het duurste artikel is {} en die kost {} Euro'
                temp2 = 'Er zijn slechts {} exemplaren in voorraad van het product met nummer {}'
                temp3 = 'In totaal hebben wij {} producten in ons magazijn liggen'
                print(temp1.format(highestpriceproduct[2],highestpriceproduct[4]))
                print(temp2.format(lowestproduct[3],lowestproduct[0]))
                print(temp3.format(str(totalproducts)))
                print('\n')
        else:
            print('File doesn\'t exist')
            filename = input('What is the filename: ')
    elif action == '3':
        filename = input('What is the filename: ')
        print('succes: ' + filename + ' is now the new name')
    elif action == '4':
        print('Goodbye')
        break
    else:
        print('That is not a option\n\n')

