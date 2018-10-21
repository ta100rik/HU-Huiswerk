


import csv

with open('gamers.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')
    highestscore = 0
    for row in readCSV:

        name = row[0]
        date = row[1]
        score = int(row[2])
        if score > highestscore:
            highestscore = score
            result = [str(score),date,name]

template = 'De hoogste score is: {} op {} behaald door {}'.format(result[0],result[1],result[2])
print(template)
