from ec import E
from millerRabin import nextprime, isprime
from math import sqrt
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
  p = nextprime((1 << 55) + random.randrange(0, 1 << 8))
  a = random.randrange(p/4, 3*p/4)
  E.params(a, -a, p)

  lb = long(p - 2*sqrt(p))
  ub = long(p + 2*sqrt(p))

  # tries 4*sqrt(p), but rho algorithm takes sqrt(p)... just BRUTE
  # let's assume professor's checking code timeouts in a minute. RUN THIS FOR FOUR MINUTES THEN 

  z = fastMult(E(1, 1), lb)
  for q in range(0, long(4*sqrt(p))):
    if q % long(4*sqrt(p)/100) == 0:
      perc = long(q/(4*sqrt(p))*100+0.5)
      print(perc)

    if z == E(0): 
      print (a, p, lb+q)
    z = z + E(1, 1)


