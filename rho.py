from ec import E

a = 12730951283832694 
p = 36028797018964019 
ph = 36028796930959053 

def f(ee, pp, qq, P, Q):
  if 0 <= ee.P[0] < p/3: return (ee + P, (pp+1)%ph, qq)
  elif p/3 <= ee.P[0] < 2*p/3: return (ee + ee, (pp*2)%ph, (qq*2)%ph)
  else: return (ee + Q, pp, (qq+1)%ph)

if __name__ == '__main__':
  E.params(a, -a, p)
  P = E(1,1)
  Q = E(32676541629070164,35161284104701659)
 
  a = f(P, 1, 0, P, Q)
  b = f(a[0], a[1], a[2], P, Q)

  cnt = 0
  while a[0].P != b[0].P:
    a = f(a[0], a[1], a[2], P, Q)
    b = f(b[0], b[1], b[2], P, Q)
    b = f(b[0], b[1], b[2], P, Q)

    cnt = cnt + 1
    if cnt % 100000 == 0: print(cnt)
  
  print (a)
  print (b)
  print (ph)

