from ec import E
import random

def fastMult(e, poww): 
  res = E(0)
  z = e

  while(poww > 0):
    res = res + (poww%2)*z
    poww = poww//2
    z = z + z
  
  return res

def test(a, p, target): 
  E.params(a, -a, p)
  s = set()
  e = E(1, 1) + E(1, 1)

  cnt = 1
  while e.P != (1, 1):
    e = e + E(1, 1)
    cnt = cnt + 1
  return cnt == target 

if __name__ == '__main__':
  p = 1000003
  trials = 100000
  target = 1000000

  for i in range(trials):
    a = random.randrange(1, p)
    E.params(a, -a, p)
    if E(0) == fastMult(E(1,1), target): # see if order(E(1, 1)) | target
      if test(a, p, target): # see if order(E(1, 1)) == target
        print(str(a) + " " + str(p))
