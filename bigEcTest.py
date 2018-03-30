from ec import E
from gcdex import inv
import random

def fastMult(e, poww): 
  res = E(0)
  z = e

  while(poww > 0):
    res = res + (poww%2)*z
    poww = poww//2
    z = z + z
  
  return res

if __name__ == '__main__':
  p = 36028797018964019 
  q = 36028796930959053 
  a = 12730951283832694 
  E.params(a, -a, p)
  s = 788139760620004
  e = 57233552642126 
  s1 = fastMult(E(1, 1), e).P[0]
  d = 8675309
  s2 = ((d + s * s1)*inv(e, q))%q

  print fastMult(E(1, 1), q)
  print fastMult(E(1, 1), s)

  print s1
  print s2
