def gcd(a, b):
  if b == 0: return a
  else: return gcd(b, a%b)

def modPow(a, k, p): 
  ret = 1
  while(k > 0): 
    if k % 2 == 1:
      ret = (ret * a) % p
    k = k / 2
    a = (a ** 2) % p
  return ret 

def millerRabinIsComposite(ev, k, q, p):
  a = modPow(ev, q, p)
  if(a == 1): return False
  else: 
    for i in range(k):
      if (a == p-1): return False
      a = (a ** 2) % p
  return True 

def isProbablePrime(n):
  if(gcd(n, 2) > 1): return False
  q = n-1
  k = 0
  while(q%2 == 0): 
    q = q / 2;  
    k = k + 1
  
  for a in [2, 3, 5, 7, 11, 13, 17, 23, 29, 31, 37, 41]:
    if millerRabinIsComposite(a, k, q, n): return False 
  return True 

def pollardAttack(a, N):
  for i in range(2, 1000000):   
    if gcd(N, a-1) > 1: 
      print "gcd("+str(N)+", "+str(a-1)+") = " + str(gcd(N, a-1))
      print i
      print a
      return True 
    a = (a * modPow(a, i, N))%N

if __name__ == '__main__':
  for a in [3]:



