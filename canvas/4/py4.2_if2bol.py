#!/usr/bin/python

leeftijd = eval(input('Geef je leeftijd: '))
passport = input('Nederlands passport (Y/N): ')

if passport == 'Y' and leeftijd >= 18:
    print('Gefeliciteerd, je mag stemmen!')
else:
    print('je mag niet stemmen')