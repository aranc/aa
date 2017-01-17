import math
from math import log, ceil, floor

def my_floor_log(x):
    return int(floor(log(x)/log(2)))

def my_ceil_log(x):
    return int(floor(log(x)/log(2)))

def c1(k,b):
    c1 = 1 << b
    i = 0
    for tmp1 in range(my_ceil_log(2*k)):
    #for tmp1 in range(my_floor_log(k)):
        t = c1 << ((b+1) << i)
        c1 = c1 | t
        i = i + 1
    #return bin(c1)
    return (c1)

#print [(2**i, bin(c1(2**i,2)).count('1')) for i in range(1,10)]

def my_bin(x, g):
    t="".join(reversed(bin(x)[2:]))
    T=""
    for i in range(len(t)):
        T += t[i]
        if i % g == g-1 :
            T += " "
    return "".join(reversed(T))
    

if True:
    k=3
    b=4
    _sum = 0
    for i in [0,1,2]:
        res = (c1(k,((b)<<i))>>(b-i))
        _sum += res
        #print i, bin(res), my_bin(res)
        print i, my_bin(res, b+1)
    #print bin(_sum)

