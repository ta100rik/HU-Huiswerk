bruin = {'boxtel','best','beukenlaan','Eindhoven','Helmond \'t Hout','Helmond','Helmond Brouwhuis','Deurne'}
groen ={'boxtel','best','beukenlaan','Eindhoven','Geldrop','Heeze','Weert'}

def bijde(set1,set2):
    list = []
    for item in set1:
        if item in set2:
            print(item)
            list.append(item)
def dif(set1,set2):
    list = []
    for item in set1:
        if item not in set2 and item is not None:
            print(item)
            list.append(item)
# run function seperate to show only the same traject or dif where the first par is the selected
# show full list of all station's
bijde(bruin,groen)
dif(bruin,groen)
dif(groen,bruin)