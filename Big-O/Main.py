import math

#  O(n)
def n(number):
    for i in range(1,n):
        print(i)



#  O(logn)
def logN(number):
    while number>1:
        number=math.floor(number/2)
        print(number)
logN(64)        