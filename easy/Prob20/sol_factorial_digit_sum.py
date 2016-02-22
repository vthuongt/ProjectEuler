from functools import reduce
from operator import mul

fac = reduce(mul, range(1,101))
digitSum = sum([int(x) for x in str(fac)])
print(digitSum)
