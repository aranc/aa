import math
from math import log, ceil, floor

def my_floor_log(x):
    return int(floor(log(x)/log(2)))

def my_ceil_log(x):
    return int(floor(log(x)/log(2)))

def c1(b, k):
    c1 = 1 << b
    i = 0
    for tmp1 in range(my_ceil_log(2*k)):
    #for tmp1 in range(my_floor_log(k)):
        t = c1 << ((b+1) << i)
        c1 = c1 | t
        i = i + 1
    #return bin(c1)
    return (c1)

#print [(2**i, c1(2,2**i).count('1')) for i in range(1,10)]

k=3
b=4
_sum = 0
for i in [0,1,2]:
    res = (c1(k>>i,((b+1)<<i)-1)>>(b-1-i))
    _sum += res
    print i, bin(res)
#print bin(_sum)

