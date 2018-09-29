invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
# making a list of the input
list = invoer.split('-')
# sorting the list to make it readable
list.sort()
# defining templates for later on
template = "gesorteede lijst van ints = {}"
template2 = "Grootste getal: {} en Kleinste getal: {}"
template3 = "Aantal getallen: {} en som  van de getallen: {}"
template4 = "Gemiddelde: {}"

def totallist(list):
    'function to get the total of the list because sum function doesn\'t work in type list'
    # defining default var
    total = 0
    # looping every list item
    for number in list:
        # counting the current total with the new list item
        total = int(number) + total
    return total
def averagelist(list):
    # grabbing totallist from other function
    total = totallist(list)
    # counting the total listitems
    total_items = len(list)
    # calculating the average price
    average = total / total_items
    return average
print(template.format(list),'\n',template2.format(max(list),min(list)),'\n',template3.format(len(list),totallist(list)),'\n',template4.format(averagelist(list)))