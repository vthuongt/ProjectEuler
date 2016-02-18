from itertools import *
from math import sqrt
import sys
import time

def gen_S():
    S = []
    a = 1
    k = 1
    yield k
    S.append(k)
    k += 1
    for l in count():
        yield S[l]
        S.append(S[l])
        for m in range(k, k + int(sqrt(S[l+1]))):
            yield m
            S.append(m)
        k = m + 1

def T_naive(n):
    return sum(islice(gen_S(), n))

def Tri(n):
    return n * (n + 1) / 2

# int(sqrt(1)) + ... + int(sqrt(n))
def sum_int_sqrt(n):
    p = int(sqrt(n))
    return p * (p - 1) * (4 * p + 1) / 6 + p * (n - p * p + 1)

class cSeq:
    def __init__(self, N):
        self.a = [ 0, 1 ]
        self.b = [ 1, 1 ]
        self.c = [ 1, 2 ]
        self.m = [ 1, 3 ]
        self.s = [ 1, 3 ]
        
        while sum(self.a) < N:
            self.add_next()
    
    def add_next(self):
        self.a.append(self.c[-1])
        self.b.append(sum_int_sqrt(self.c[-1]))
        self.c.append(self.a[-1] + self.b[-1])
        self.m.append(self.c[-1] + self.m[-1])
        self.s.append(Tri(self.c[-1]))
    
    def length(self):
        return len(self.s)

def T(n):
    def next_s((k, p, r, q, sr, num, s), l):
        a = orig.a[k]
        c = orig.c[k]
        first, last = r
        num1 = num + first + l - 1 - a
        s1 = s + Tri(first + l - 1) - Tri(a)
        sr1 = sum_int_sqrt(first + l - 1) - sum_int_sqrt(a) + sr
        first1 = c + sr1 + 1
        if l == 0:
            last1 = first1 + int(sqrt(first))
            return (k + 1, p, (first1, last1), first, sr1, num1, s1)
        elif l == last - first:
            last1 = first1 + int(sqrt(q))
            return (k + 1, last - 1, (first1, last1), q, sr1, num1, s1)
        else:
            last1 = first1 + int(sqrt(first + l))
            return (k + 1, first + l - 1, (first1, last1),
                    first1 + 1, sr1, num1, s1)
    
    def end(status):
        for k in range(status[0] + 1, L):
            status = next_s(status, status[2][1] - status[2][0])
        return status[-2] + orig.m[-3]
    
    def find(status, first, last):
        if first == last - 1:
            return first
        
        mid = (first + last) / 2
        s = next_s(status, mid - 1)
        if end(s) < n:
            return find(status, mid, last)
        else:
            return find(status, first, mid)
    
    orig = cSeq(n)
    L = len(orig.a)
    status = (1, 1, (2, 3), 1, 0, 1, 1)
    for k in range(2, L):
        l = find(status, 0, status[2][1] - status[2][0] + 1)
        status = next_s(status, l)
    return sum(orig.s[:-2]) + status[-1]

t0 = time.clock()
N = 10 ** 18
D = 10 ** 9
print T(N) % D
print >>sys.stderr, time.clock() - t0