cost = 4356
persons = int(input('aantal pesons'))
try:
    result = cost/persons
    if result < 0:
        print('Dit is een negatief getal dit is niet mogelijk')
    else:
        print(result)

except ZeroDivisionError:
    print('Je kan het niet delen door 0')
except ValueError:
    print('')
except:
    print('Fout ingevuld')