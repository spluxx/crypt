from ec import E

p = 977245356317
ph = 977244806323

def fastMult(e, poww): 
  res = E(0)
  z = e

  while(poww > 0):
    res = res + (poww%2)*z
    poww = poww//2
    z = z + z
  
  return res

if __name__ == '__main__':
  E.params(454619944748, 67189121909, p)
  P = E(474177197796,218937542115)
  Q = E(287274742986,103070012816)

  print(fastMult(P, 777244806324))

  E.params(508139, -508139, 900001)
  print(fastMult(E(1, 1), 10000))
