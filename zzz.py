'''
Created on Nov 29, 2017

@author: jwf888
'''

from ec import E
import gcdex 
import math
 
def doubleAndAdd(P, n): 
    R = E(0)
    Q = P
    while n > 0:
        if (n%2) == 1: R = R + Q
        n = n//2
        Q = Q + Q
    return R
 
def order(a):
    s = set((1,1))
    count = 0
    Q = E(1,1)
    while (Q+E(1,1)).P not in s:
        Q = Q + E(1,1)
        s.add(Q.P)
        count += 1
    print(count)
    return count

def check(p):
    a = 1
    E.params(a, -a, p)

    while True:
      a += 1
      E.params(a, -a, p)
      if doubleAndAdd(E(1,1), 1000000) == E(0):
        print(a)
        if order(a) == 1000000:
          return a
     
print(check(1000003))

