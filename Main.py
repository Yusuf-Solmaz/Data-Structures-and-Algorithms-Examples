import math

def logN(number):
    while number>1:
        number=math.floor(number/2)
        print(number)

logN(64)        