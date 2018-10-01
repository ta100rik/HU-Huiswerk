def code(string):
    word = ''
    for char in string:
        dec = ord(char) + 3
        new_value = chr(dec)
        word = word + new_value
    return word

gebruiker = input('Give me your name plz: ')
Startstation = input('Where do the user starts: ')
endstation = input('Where do the users stops: ')

combine = gebruiker+Startstation+endstation
print(code(combine))