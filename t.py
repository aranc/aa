import math
from math import log, ceil, floor

def my_floor_log(x):
    return int(floor(log(x)/log(2)))

def c1(b, k):
    c1 = 1 << b
    i = 0
    for tmp1 in range(my_floor_log(2*k)):
    #for tmp1 in range(my_floor_log(k)):
        t = c1 << ((b+1) << i)
        c1 = c1 | t
        i = i + 1
    return bin(c1)

print [(2**i, c1(2,2**i).count('1')) for i in range(1,10)]
