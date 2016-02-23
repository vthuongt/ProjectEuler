import math
import time

def getDiv(n):
    s = {1}
    for i in range(1,math.floor(math.sqrt(n+1))):
        if n%i == 0:
            s |= {i,n//i}
    s -= {n}
    #print(s)
    return s

def isAbundant(n):
    return True if sum(getDiv(n))>n else False

