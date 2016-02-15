'''
Created on 15.02.2016

@author: Viet
'''
# fractal sequence
import math
def f(n):
    return math.floor(n**0.5)
"""
for i in range(1,10**2):
    print(str(i)+": "+ str(f(i)))
"""

def getNextCircledNumber(S,Circ):
    #iS,    iCirc
    for i in range(-1,-len(S)-1,-1):
        if Circ[i]:
            return S[i]+1
    

def nextNumbers(S, Circ):
    nS,nCirc = S, Circ

    if Circ[-1] == False:
        nS += [getNextCircledNumber(S,Circ)]   
        Circ += [True]
    else:
        newSuncirc = S[len(S) - Circ.count(True)]
        numCirc = f(newSuncirc)
        for i in range(0,numCirc-1):
            nS+= [getNextCircledNumber(S,Circ)]
            Circ += [True]
        nS+= [newSuncirc]
        Circ+= [False]        
        
    return [nS,Circ]

def printing(S,Circ):
    for i in range(0,len(S)):
        if Circ[i]:
            print("["+str(S[i])+"]",end=' ')
        else:
            print(str(S[i]), end=' ')
    print()


n = 10**18
S,Circ  = [1],[True]
while len(S)<n:
    S,Circ = nextNumbers(S,Circ)

#printing(S,Circ)
print("T("+str(n)+")="+str(sum(S)))
print("last 9 digits: "+str(sum(S))[-9:])
