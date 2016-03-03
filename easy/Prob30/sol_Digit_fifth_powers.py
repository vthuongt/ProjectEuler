
def val(n):
    s = str(n)
    value = 0
    for i in s:
        value += int(i)**5
    return value

# finding max value to test to
nmax = 9
while nmax < val(nmax):
    nmax = nmax*10+9

#print(str(nmax)+">"+str(val(nmax)))

print(sum([x for x in range(2,nmax+1) if val(x)==x]))