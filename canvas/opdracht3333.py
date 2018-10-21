import random
def chooseCharacter(apilst):
    allCharacters = apilst #read api list
    charlst = [] #create fresh list for char names
    descriplst = [] #create fresh list for descriptions

    for character in allCharacters:
        charlst.append(character['name']) #add char to char list
        descriplst.append(character['description']) #add descrip to descrip list

    randomselect = random.choice(charlst) #select random char
    while True:
        descriptionchar = descriplst[charlst.index(randomselect)]
        # looking if the chars of the description are longer than 1 or equals to 1
        if len(descriptionchar) >= 1:  # if descrip of selected char >1 let prog know
            print('{}'.format(randomselect))
            break
        else:  # if descrip of selected char non exist let prog know
            randomselect = random.choice(charlst)





    return{'character':randomselect,'description':descriptionchar} #return character and descrip for later use