#!/usr/bin/python

CijferProg = 9

Cijfericor = 6
CijferCSN = 7

Gemiddelde = (Cijfericor+CijferProg+CijferCSN) / 3

Beloning = (Cijfericor * 30) + (CijferProg * 30) + (CijferCSN * 30)

Overzicht = 'Mijn cijfer ' + str(Gemiddelde) + ' leveren een beloning op van ' + str(Beloning)

print(Overzicht)