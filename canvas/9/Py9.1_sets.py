# this assignment is the right one sorry for the other code didn't noticed the build in methods for sets
bruin = {'boxtel','best','beukenlaan','Eindhoven','Helmond \'t Hout','Helmond','Helmond Brouwhuis','Deurne'}
groen ={'boxtel','best','beukenlaan','Eindhoven','Geldrop','Heeze','Weert'}

print(bruin.intersection(groen))
print(bruin.difference(groen))
print(groen.difference(bruin))

# this under part is correct code but is with list
# the above assignment is the good answer but have a look to the one below


# def bijde(set1,set2):
#     list = []
#     for item in set1:
#         if item in set2:
#             print(item)
#             list.append(item)
# def dif(set1,set2):
#     list = []
#     for item in set1:
#         if item not in set2 and item is not None:
#             print(item)
#             list.append(item)
# run function seperate to show only the same traject or dif where the first par is the selected
# show full list of all station's
# bijde(bruin,groen)
# dif(bruin,groen)
# dif(groen,bruin)
