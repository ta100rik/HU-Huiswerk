def som(getalLijst):
    result = 0
    for number in getalLijst:
        result = result + number

    return result

lijst = [1,4,2,3,4,12,3,213,213,213,123]
print(som(lijst))