from itertools import permutations
from functools import reduce
import time

start = time.time()
perms = sorted(list(permutations(range(0,10))))
temp = perms[999999]
print(temp)
print(str(reduce(lambda x,y: x+y, map(str,temp))))
end = time.time()
print("Time elapsed: "+str(end-start))
