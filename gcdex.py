#!/usr/bin/env python

import sys

def gcd(a, b):
    if b==0:
        return (a)
    g = a
    y = b
    while y != 0:
        t = g % y
        g = y
        y = t
    return g
    

# HPS ex 1.12
def gcdex(a, b):
    if b==0:
        return (a, 1, 0)
    u = 1
    g = a
    x = 0
    y = b
    while y != 0:
        (q, t) = divmod(g, y)
        s = u - q*x
        u = x
        g = y
        x = s
        y = t
    u %= (b//g) # 1.2(e) almost: u might be 0
    v = (g - a*u)//b
    return (g,u,v)


def inv(a, m):
    (gcd, b, _) = gcdex(a,m)
    if gcd != 1:
        raise ArithmeticError
    return b

# This is a standard Python trick:
# The following is run only if this file is run as a program
if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    (d,u,v) = gcdex(a,b)
    print("{} = {}*{} + {}*{}".format(d,u,a,v,b))

