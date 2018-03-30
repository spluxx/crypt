def gcduvAux(a, b, u, g, x, y):
  if(y == 0): return (g, u, (g-a*u)/b)
  else:
    q = g/y
    t = g%y
    s = u-q*x
    return gcduvAux(a, b, x, y, s, t)

def gcduv(a, b):
  (g, u, v) = gcduvAux(a, b, 1, a, 0, b)
  while u > 0:
    u -= b/g
    v += a/g

  while u < 0:
    u += b/g
    v -= a/g

  return (g, u, v)
    
def mod_inv(a, p):
  return gcduv(a, p)[1]

def residue(a, p):
  while a < 0:
    a += p
  return a % p

def mod_polyadd(a, b, p):
  if len(b) > len(a):
    t = a    
    a = b
    b = t

  dega = len(a)-1
  degb = len(b)-1

  q = [0 for _ in range(len(a)-len(b))]
  for eb in b: q.append(eb)

  for i in range(dega+1):
    q[i] = residue(q[i]+a[i], p)

  z = -1
  for i in range(len(q)):
    if q[i] != 0: 
      z = i
      break
  
  r = []
  if z >= 0:
    for i in range(z, len(q)):
      r.append(q[i]) 

  return r

def mod_polysub(a, b, p):
  return mod_polyadd(a, [residue(-x, p) for x in b], p)

def mod_polymul(a, b, p): 
  q = []
  dega = len(a)-1
  degb = len(b)-1

  for i in range(dega+degb, -1, -1):
    c = 0
    for j in range(dega+1):
      if 0 <= i-j < degb+1:
	c += a[j]*b[i-j]
    q = [residue(c, p)] + q

  return q


def mod_polydiv(a, b, p): # (q, r) where a = bq + r (assuming deg(a) >= deg(b))
  d = len(a) - len(b)
  q = []
  for i in range(len(a)): a[i] = residue(a[i], p)
  for i in range(len(b)): b[i] = residue(b[i], p)

  for i in range(d+1):
    m = residue(mod_inv(b[0], p) * a[i], p)
    q.append(m)
    for j in range(len(b)):
      a[j+i] = residue(a[j+i]-b[j]*m, p)

  z = -1
  for i in range(len(a)):
    if a[i] != 0: 
      z = i
      break
  
  r = []
  if z >= 0:
    for i in range(z, len(a)):
      r.append(a[i]) 

  return (q, r)
  
def poly_str(a):
  empty = True
  for ea in a: 
    if ea != 0: 
      empty = False
  if empty: return "0"
  else:
    ret = ""
    for i in range(len(a)):
      if i < len(a)-1:
        ret += str(a[i])+"x^"+str(len(a)-i-1)+" + "
      else:
        ret += str(a[i])+"x^"+str(len(a)-i-1)
    return ret

def poly_gcd(a, b, p):
  oa = [x for x in a]
  ob = [x for x in b]

  while True:
    print poly_str(a)
    print poly_str(b)
    (q, r) = mod_polydiv(a, b, p)
    print poly_str(q)
    print poly_str(r)
    print ""

    if len(r) == 0:
      print "GCD(" + poly_str(oa) + ", "+ poly_str(ob) + ") MOD " + str(p) + " = " + poly_str(b)
      break

    a = b
    b = r

def poly_gcduv(a, b, p):
  oa = [x for x in a]
  ob = [x for x in b]

  (u0, v0) = ([1], [0]) ## a = 1a+0b :: r0
  (u1, v1) = ([0], [1]) ## b = 0a+1b :: r1

  while True:
    (q, r) = mod_polydiv(a, b, p)
    
    r2u = mod_polysub(u0, mod_polymul(q, u1, p), p)
    r2v = mod_polysub(v0, mod_polymul(q, v1, p), p)

    (u0, v0) = (u1, v1)
    (u1, v1) = (r2u, r2v)

    if len(r) == 0: break

    a = b
    b = r

  return (b, u0, v0)

if __name__ == '__main__':
  p = 7
  a = [1, 3, -5, -3, 2, 2]
  b = [1, 1, -2, 4, 1, 5]
  pa = [x for x in a]
  pb = [x for x in b]

  (g, u, v) = poly_gcduv(pa, pb, p)

  print "["+poly_str(a) + "] * ["+poly_str(u) + "] + \n" + "["+poly_str(b) + "] * ["+poly_str(v) + "] = [" + poly_str(g) + "]"

  print poly_str(mod_polyadd(mod_polymul(a, u, p), mod_polymul(b, v, p), p))
