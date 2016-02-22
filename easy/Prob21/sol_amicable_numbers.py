import math

def getSumOfDiv(n):
    s = {1}
    for i in range(1,math.floor(math.sqrt(n+1))):
        if n%i == 0 and not (i**2==n):
            s |= {i,n//i}
    s -= {n}
    #print(s)
    return sum(s)

maxN = 10000
L = [getSumOfDiv(x) for x in range(1,maxN)]
LL = [x+1 for x in range(0,maxN-1) if L[x]-1<maxN and L[L[x]-1]== x+1 and L[x]-1 != x ]
print(LL)
print(sum(LL))