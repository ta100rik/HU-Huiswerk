def gemiddelde(uservalue):
    #splitting the current user string
    uservalue = uservalue.split(' ')
    # counting the words in the list
    wordscount = len(uservalue)
    # making a global count var for counting the chars in every word
    Totaallen = 0
    # looping for every word
    for woord in uservalue:
        # counting the words and counting it with the current filled var
        Totaallen = len(woord) + Totaallen
    # after we got the words count and chars counted we can just calculate the average word lengths
    calculate = Totaallen / wordscount
    # return the calculation
    return calculate
# asking the user input
uservalue = input('Voer hier u zin in: ')
# putting the user answers in a var
result = gemiddelde(uservalue)
# printing the result
print(result)
