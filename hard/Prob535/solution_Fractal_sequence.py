'''
Created on 15.02.2016

@author: Viet
'''
# fractal sequence
import math
import cProfile
def f(n):
    return math.floor(n**0.5)

 
def nextNumbers(S, Circ, numMarked):
    if Circ[-1] == False:
        S += [numMarked+1]   
        Circ += [True]
        numMarked+=1
    else:
        newSuncirc = S[len(S) - numMarked]
        numCirc = f(newSuncirc)
        for i in range(0,numCirc-1):
            S+= [numMarked+1]
            Circ += [True]
            numMarked+=1
        S+= [newSuncirc]
        Circ+= [False]        
        
    return [S,Circ,numMarked]

def printing(S,Circ):
    for i in range(0,len(S)):
        if Circ[i]:
            print("["+str(S[i])+"]",end=' ')
        else:
            print(str(S[i]), end=' ')
    print()


def main1(n):
    S,Circ, numMarked  = [1],[True],1
    while len(S)<n:
        S,Circ, numMarked = nextNumbers(S,Circ, numMarked)
    
    #print(str(n)+": "+str(n-numMarked))#, end='')
    #printing(S,Circ)
    print("T("+str(n)+")="+str(sum(S)))
    #print("last 9 digits: "+str(sum(S))[-9:])
    
def main2(n):
    S = [1]
    i = 0
    while len(S)<n:
        i+=1
        L=[]
        counter = 0
        for x in S:
            num = f(x)
            L +=list(range(counter+1,counter+num+1))
            counter += num
            L+=[x]
        S = L.copy()
        #print(str(i)+": "+str(len(S)))
    printing2(S,n)
    #print("T("+str(n)+")="+str(sum(S[0:n])))
    
def printing2(S,n):
    maxKnown = 0
    for i in range(0,n):
        if maxKnown < S[i]:
            print("["+str(S[i])+"]",end=' ')
            maxKnown+=1
        else:
            print(str(S[i]), end=' ')
    print()
        
#cProfile.run('main1(10**6)')
#cProfile.run('main2(10**9)')
#for i in range(10**3,10**4):

for i in range(1,50):
    main2(i)

#for i in range(1,10):
#    print(str(i)+": "+ str(f(i)))
