import time

def val(n):
    s = str(n)
    value = 0
    for i in s:
        value += int(i)**5
    return value

def val2(n):
    value = 0
    while n != 0:
        value += (n%10)**5
        n= n//10
    return value
# finding max value to test to

nmax = 9
while nmax < val(nmax):
    nmax = nmax*10+9

#print(str(nmax)+">"+str(val(nmax)))
start = time.time()
print(sum([x for x in range(2,nmax+1) if val(x)==x]))
end = time.time()
print(sum([x for x in range(2,nmax+1) if val2(x)==x]))
end2 = time.time()

print("Time1: "+str(end-start))

print("Time2: "+str(end2-end))