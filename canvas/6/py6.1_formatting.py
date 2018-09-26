def convert(Graden):
   result =  Graden * 1.8 + 32
   return result

def table():

    print(' F        C')
    for temp in range(-30,41,10):
        Fahrenheit =  convert(temp)
        print(str(Fahrenheit) + '    ' + str(temp))

table()