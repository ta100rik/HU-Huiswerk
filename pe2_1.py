#!/usr/bin/python

verdienperuur = eval(input('Wat verdien je per uur: '))
uurgewerkt = eval(input('Hoeveel uur heb je gewerkt: '))

totaal = str(uurgewerkt * verdienperuur)
verdienperuur = str(verdienperuur)
print(verdienperuur + ' uur werken levert ' + totaal + ' euro op')