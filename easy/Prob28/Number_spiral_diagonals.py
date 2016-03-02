import math


#1001 by 1001 square
#upper right corner numbers are squares 
#all other number follow therefrom

n = 1001
ruSeq = [1]

while ruSeq[-1] < n**2:
    ruSeq +=[int(4*math.sqrt(ruSeq[-1])+4+ruSeq[-1])]
    
#print(ruSeq)
# summing up all corners
s = 1
for i in ruSeq[1:]:
    sidelength = math.sqrt(i)-1
    #print(4*i -6* (sidelength))
    s += 4*i -6* (sidelength)
    #print('{0}, {1}, {2}, {3}'.format(i, i-sidelength, i-2*sidelength, i-3*sidelength))

print(int(s))
