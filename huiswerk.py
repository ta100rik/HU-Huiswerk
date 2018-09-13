#!/usr/bin/python
#
#
# # 2.1 practice problem
# # A
# print ((1+2)/(3+4+5))
# # B
# ages = [23,19,31]
# print(int(sum(ages)/len(ages)))
# # C
# print(403//73)
# # D
# print(403%73)
# # e
# print(2**10)
# # F
# saralen = 54
# marklen = 75
# print(abs(saralen-marklen))
# # G
# prices = [34.99, 29.95, 31.50]
# print(min(prices))
#
# # 2.3
#
# # A
# a = 3
# print(a)
# # B
# b = 4
# print(b)
# # C
# c = a * a + b * b
# print(c)
#
# # 2.5
#
# s = '0123456789'
# # A
# print(s[0])
# # B
# print(s[1])
# # C
# print(s[6])
# # D
# print(s[-2])
# # E
# print(s[-1])
#
# # 2.6
# words = ['bat', 'ball', 'barn', 'basket', 'badminton']
#
# print(words[0] in words)
# print (words[-1] not in words)
#
# # 2.7
# grades = [9, 7, 7, 10, 3, 9, 6, 6, 2]
#
# # A
# print(grades.count(7))
#
# # B
# grades.append(4)
# print(grades)
# # C
# print(max(grades))
#
# # D
# grades.sort()
# print(grades)
#
# # E
# averagegrade = (sum(grades)/len(grades))
# print(averagegrade)
#
# # 2.8
#
# # a
# #  first the 2+3 than looking if it is equal to 4 and making it true or false if it is false look up what is after the or statement
#
# # B
# # first the multiplier than the different lookup if it is smaller than -10 and than look if it is 0
#
# # C
# # same as above but than with 2 checks of boolean and than check if it is a true or 0 and return true or false depending on the result
#
# # D
# #6 ** 2 as last
#
# # E
# # check if 2 is in the objects  as last
#
#
# import math
#
# # 2.10
#
# # A
# a = 2
# b = 2
# hypo = (a**2)+(b**2)
# calc_hypo = math.sqrt(hypo)
# print(calc_hypo)
#
# # B
#
# check1 = (calc_hypo < 5)
# print(check1)
# # C
# Area = math.pi * (a**2)
# print(Area)
#
# # D
#
# Rad = 2
# check2 = (a**2 + b**2 <= Rad**2)
# print(check2)





# 3.1

# fahrenheit = input('Enter your Fahrenheit:')
# fahrenheit = eval(fahrenheit)
# Celsiuis = 5/9 * (fahrenheit - 32)
# print(Celsiuis)

# 3.2

# A

# personage = input('What is your age')
# personage = eval(personage)

# if personage > 62:
#     print('You can get your pension benefits: ')

# B

# names = ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth'];
# personname = input('What is your name: ')

# if personname in names:
#     print('one of the top 5 baseball players')


# C

# hits = input('How many hits do you have: ')
# schield = input('How many schield point do you have: ')
#
# hits = eval(hits)
# schield = eval(schield)
#
# if hits > 10 and schield == 0:
#     print('You are dead...')

#D

# directions = ['north','south','east','west']


# userdir = input('Type in your direction')
#
# if userdir in directions:
#     print('You are save');

# year = 2016;
#
# if (year % 4) == 0:
#     print('This could be a leap year')
# else:
#     print('This is not a leap year')
#
#
# ticket = [1,2,3,4,5,6,7,8,9]
# lottery = ['1',9,9,9,9,9,9,9,9]
#
# if len(ticket) == len(lottery):
#     print('You won!')
# else:
#     print('You lost')

#3.4


# userlist = ['joe', 'sue','hani', 'sophie','zyad']
# userid = input('Enter your login id: ')
#
# if userid in userlist:
#     print('You are in')
# else:
#     print('User unkown')
# print('done')
#

# 3.5

# wordlist = ['chair','cat','dog','amersfoort','Utrecht']
#
# for word in wordlist:
#     if len(word) == 5:
#         print(word)
#

# 3.6

# A

# for number in range(10):
#     print(number)
#

# B

# for number in range(2):
#     print(number)

# 3.7

# A
# for number in range(13):
#     if number >= 3 and number <= 12:
#         print(number)

# B

# for number in range(0,9,2):
#     print(number)

# C

# for number in range(0,24,3):
#     print(number)

# D

# for number in range(3,12,5):
#     print(number)

# 3.8

def perimeter(R):
    if type(R) == 'String':
        R = eval(R)
    if (R + abs(R)) != 0:
        R = float(abs(R))
        import math
        perimeters = 2 * math.pi * R
        return perimeters
    else:
        return 'your variable is not a positive number'
# number = input('insert your number:')
# print(perimeter(number))

# 3.9
def average(First,Second):
    if type(First) == 'String':
        First = eval()
    if type(Second) == 'String':
        Second = eval()

    result = (First+Second) / 2;
    return result

# print(average(1,3))

# 3.10

def noVowel(s):
    vowels = ['a','e','i','o','u']
    isthere = False
    for char in s:
       if char in vowels:
           isthere = True
    return isthere

# print(noVowel('cm'))

# 3.11

def allEven(list):
    'This shows if all the list item are even '
    checkbol = True
    for number in list:
        if checkbol:
            if (number % 2) == 1:
                checkbol = False;
    return checkbol

# list = [8,0,-2,4,-6,10]
# print(allEven(list))
help(allEven)







