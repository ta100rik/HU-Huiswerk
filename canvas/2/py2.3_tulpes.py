#!/usr/bin/python

import string
string.letters = 'ABC'
import random
i = 0
list = []
while i < 6:
  list.append(random.choice(string.letters))
  i += 1

print(list)

A = list.count('A')
B = list.count('B')
C = list.count('C')

countedlist = [A,B,C]

print(countedlist)