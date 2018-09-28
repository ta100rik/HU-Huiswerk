def seizoen(monthnumber):
    # checking if it is a possible month number
    if monthnumber <= 12 and monthnumber > 0:
        # a list of the different seazons
        winter = [12,1,2]
        lente = [3,4,5]
        zomer = [6,7,8]
        herfst = [9,10,11]
        # Because python doesn't have a case switch for some reason we us if elif
        if monthnumber in winter:
            result = 'winter'
        elif monthnumber in lente:
            result = 'lente'
        elif monthnumber in zomer:
            result = 'zomer'
        else :
            result = 'herfst'
    else:
        # this will run if the number given is bigger than 12 or smaller or equal to 0
        result = 'This is not a month number'
    return result
# asking user input
userinput = eval(input('Give us your Month number: '))
# putting result in var
result = seizoen(userinput)
# printing the result
print(result)