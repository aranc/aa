import math
from math import log, ceil, floor

def my_floor_log(x):
    return int(floor(log(x)/log(2)))

def my_ceil_log(x):
    return int(floor(log(x)/log(2)))

def _c1(k,b):
    c1 = 1 << b
    i = 0
    for tmp1 in range(my_ceil_log(2*k)):
    #for tmp1 in range(my_floor_log(k)):
        t = c1 << ((b+1) << i)
        c1 = c1 | t
        i = i + 1
    #return bin(c1)
    return (c1)

def c1(k, b):
    return ((1-(1<<((b+1)*2*k)))/(1-(1<<(b+1))))<<(b)

print [(2**i, bin(c1(2**i,2)).count('1')) for i in range(1,10)]

def my_bin(x, g):
    t="".join(reversed(bin(x)[2:]))
    T=""
    for i in range(len(t)):
        T += t[i]
        if i % g == g-1 :
            T += " "
    i += 1
    while i % g != 0:
        i += 1
        T += "0"
    return "".join(reversed(T))
    

def try1():
    k=3
    b=4
    _sum = 0
    for i in [0,1,2]:
        res = (c1(k,((b+1)<<i)-1)>>(b-i))
        _sum += res
        #print i, bin(res), my_bin(res)
        print i, my_bin(res, b+1)
    #print bin(_sum)

def try2():
    k=3
    b=4
    _sum = 0
    for i in [0,1,2]:
        res = (c1(k,((b+1)<<i)-1)>>(b-i))
        _sum += res
        #print i, bin(res), my_bin(res)
        print i, my_bin(res, b+1)
    #print my_bin(_sum, b+1)

#try2()

def goal():
    print "0001 0000 0001 0000 0001 0000 0001 0000"
    print "0010 0010 0000 0000 0010 0010 0000 0000"
    print "0100 0100 0100 0100 0000 0000 0000 0000"
    print "0111 0110 0101 0100 0011 0010 0001 0000"
#goal()

def ct(k,b):
    c1 = (1 << b) + 1
    i = 0
    for tmp1 in range(my_ceil_log(2*k)):
    #for tmp1 in range(my_floor_log(k)):
        t = c1 << ((b+1) << i) + 1
        c1 = c1 + t
        i = i + 1
    #return bin(c1)
    return (c1)
#print my_bin(ct(3, 4), 4+1)

def _c2(k, b):
    return ((c1(k,b)>>b) ** 2) & ((1<<(2*k*(b+1))) - 1)

