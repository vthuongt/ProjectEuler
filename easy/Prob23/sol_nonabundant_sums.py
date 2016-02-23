import math
import time

def getDiv(n):
    s = {1}
    for i in range(1,math.ceil(math.sqrt(n+1))):
        if n%i == 0:
            s |= {i,n//i}
    s -= {n}
    #print(s)
    return s

def isAbundant(n):
    return True if sum(getDiv(n))>n else False

def isExpressable(n):
    for i in range(1,n):
        if i in abundantNums and n-i in abundantNums :
            print(str(n)+"="+str(i)+"+"+str(n-i))
            return True
    return False


abundantNums = {12}
for n in range(13,28124):
    if isAbundant(n):
        abundantNums |= {n}
        
integers = []
for n in range(1,28124):
    if not isExpressable(n):
        integers+= [n]
        
print(integers)
print(sum(integers))
print(sorted(list(abundantNums)))
