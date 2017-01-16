import math
from math import log, ceil, floor

def c1(b, k):
    c1 = 1 << b
    i = 0
    for _ in range(int(floor(log(2*k)/log(2)))):
        i = i + 1
        t = c1 << ((b + 1) * i)
        c1 = c1 | t
    return bin(c1)

print [(i, c1(2,i).count('1')) for i in range(1,10)]
