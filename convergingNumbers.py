# I want to create a function that calculates the power of 2 to the nth power and returns the result
# I want to create a function that calculates the power of 2 to the nth power and returns the result
import datetime
from numba import njit
import matplotlib.pyplot as plt
import numpy as np



# I want to calculate the last 10 digits of a number and compare to another number
def lastTenDigits(n):
    # I want to convert the number to a string
    n = str(n)
    # I want to return the last 10 digits
    return n[-10:]




# i want a loop that multiplies increments of 1024 for 1000000 times
sameValue = True
"""for n in range(200000, 1000000):
    # I want to multiply the number by 1024
    twoPowerTen = powerOfTwo(10) ** n
    twoPowerTenTwo = powerOfTwo(10) ** (n + 1)
    l = lastTenDigits(twoPowerTen)
    l2 = lastTenDigits(twoPowerTenTwo)
    if l == l2 and sameValue:
        print("Same value " + str(twoPowerTen))
        sameValue = False
    if l == l2 and not sameValue:
        print("Same value")
    print(n)"""



# I want to print 2 ** 10 ** n in a loop

d = datetime.datetime.now()
def performanceTest():
    y = np.array([2 ** 10 ** n for n in range(1000000)])

print(datetime.datetime.now() - d)

d = datetime.datetime.now()
@njit
def performanceTestNjit():
    y = np.array([2 ** 10 ** n for n in range(1000000)])

print(datetime.datetime.now() - d)


performanceTest()
performanceTestNjit()
