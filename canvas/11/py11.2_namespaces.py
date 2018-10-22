# 1
def verdubbelnummer(number):
    number = number + number
    return number

nummer = 7
result = verdubbelnummer(nummer)
print(result)
# 2
import time
temp = "%H:%M:%S"
currenttime = time.strftime((temp))
print(currenttime)

# 3
def plusvijftien(nummer):
    som = 15 + nummer
    return som
def verdubbelplus1(nummer):
    result = 2 * nummer
    result = result + 1
    return result

nummer = 3
res = plusvijftien(nummer) + verdubbelplus1(nummer)
print(res)


