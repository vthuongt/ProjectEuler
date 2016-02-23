def getNextFibNum(a):
    return a[0]+a[1]

FibSeq = [1,1]
temp = 0
while len(str(temp))<1000:
    FibSeq +=[getNextFibNum(FibSeq[-2:])]
    temp = FibSeq[-1]
    
#print(FibSeq)
print(temp)
print(len(FibSeq))