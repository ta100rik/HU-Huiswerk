def convert(Graden):
   result =  Graden * 1.8 + 32
   return result

def table():
    template = '{:5} {:2}'
    print(template.format('F','C'))
    for temp in range(-30,41,10):
        Fahrenheit = convert(temp)
        print(template.format(str(Fahrenheit),str(temp)))
table()