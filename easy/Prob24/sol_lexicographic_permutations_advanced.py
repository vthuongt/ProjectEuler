from functools import reduce
import time
def all_perms(elems):
    if(len(elems))<=1:
        yield elems
    else:
        for perm in all_perms(elems[1:]):   #perm is element of list/generator with all permutation without the first elem
            for i in range(len(elems)):     #loops over all possible positions of the firste element in those permutations
                yield perm[:i] + elems[0:1]+ perm[i:]
                

start = time.time()                
perms = sorted(list(all_perms(list(range(0,10)))))
temp = perms[999999]
print(temp)
print(str(reduce(lambda x,y: x+y, map(str,temp))))
end = time.time()
print("time elapsed: "+str(end-start))