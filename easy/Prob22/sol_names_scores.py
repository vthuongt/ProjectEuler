import re
import time


def scoring(name):
    return sum([ord(x) for x in name])-64*len(name)

f = open('names.txt', 'r')
s = f.read()
f.close()
names = re.sub('"', '', s).split(',')
names = sorted(names)
start = time.time()
scores = list(map(lambda name: (sum([ord(x) for x in name])-64*len(name))*(names.index(name)+1), names))
end1 = time.time()
scores = list(map(scoring,names))
for i in range(0,len(scores)):
    scores[i]*=(i+1)
end2 = time.time()
print(sum(scores))

print(end1 - start)
print(end2-end1)
#==> map version less readable and slower