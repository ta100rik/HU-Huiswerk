def only4chars(list):
    newlist = []
    for word in list:
        if len(word) == 4:
            newlist.append(word)
    return newlist
def stringsinlist(list):
    counter = 0
    for item in list:
        if isinstance(item, str):
            counter += 1
    if counter >= 10:
        result = True
    else:
        result = False
    return result

List = eval(input("Geef lijst met minimaal 10 strings: "))

# checking if there are 10 or more strings
check = True if stringsinlist(List) else False
if check:
    result = only4chars(List)
    template = 'De nieuw-gemaakte lijst met alle vier-letter strings is:{}'
    print(template.format(result))
else:
    template = 'The list doesn\'t has more or 10 strings in it run again'
    print(template)