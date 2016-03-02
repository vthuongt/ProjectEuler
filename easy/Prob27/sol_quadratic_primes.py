
def hasDiv(n):
    global primes
    for p in primes:
        if n%p==0:
            return True
    return False
    
def isPrime(n):
    global primes
    global maxPrime
    primeCandidate = maxPrime
    while n>= maxPrime:
        primeCandidate += 2
        if not hasDiv(primeCandidate):
            maxPrime = primeCandidate
            primes += [primeCandidate]
        
        
    if n == maxPrime or n in primes:
        return True
    else:
        return False
        
def checkPrimeSeq(a,b):
    global primes
    global maxPrime
    n = 0
    while isPrime(n**2+a*n+b):
        n += 1
        #temp = isPrime(n**2+a*n+b)
        #print("{0}: {1}".format(n,n**2+n+41))
    return n


primes = [2,3]
maxPrime = 3
maxLengths = {}
for a in range(-999,1000):
    for b in range(-999,1000):
        lenPrimeSeq = checkPrimeSeq(a,b)
        #print("n^2{0:+}n{1:+} has {2} consequtive primes".format(a,b,lenPrimeSeq))
        maxLengths[(a,b)]  =lenPrimeSeq

        
maxKey = max(maxLengths.keys(),key= lambda x: maxLengths[x]) 
print(maxKey)
print(maxKey[0]*maxKey[1])
print(maxLengths[maxKey])
#print("longest consecutive prime numbers with coefficients"+ 
#"(a,b)={0} with {1} primes """.format(maxKey,maxLengths[maxKey]))