grondgetallen = [2,2,-12]

def kwadraten_som(grondgetal):
    result = 0
    for number in grondgetal:
        if number > 0:
            kwadrant = number ** 2
            result = result + kwadrant
    return result

print(kwadraten_som(grondgetallen))