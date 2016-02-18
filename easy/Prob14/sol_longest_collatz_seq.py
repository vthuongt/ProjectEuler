from itertools import count
chainLengths = {1:1}
for i in range(2, 10**6):
    temp, count = i,0
    while not (temp in chainLengths):
        temp = temp/2 if temp%2==0 else 3*temp+1
        count +=1
    count += chainLengths[temp]
    chainLengths[i]= count
print("finished")
print(max(chainLengths.keys(),key=(lambda x: chainLengths[x])))