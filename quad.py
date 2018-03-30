def solutions(modulo, N):
  n = N % modulo
  for x in range(1, modulo/2+1):
    if (x*x) % modulo == n:
      return (x, modulo-x)
  return (0, 0)

if __name__ == '__main__':
  N = 493
  fr = 23
  to = 50 
  B = 16
  plim = 10000
  lis = []

  for t in range(fr, to):
    lis.append(t*t-N)

  pp = list()
  qq = set()

  for i in range(2, plim):
    if i not in qq:
      z = i
      sub_p = list()
      while z < plim:
	sub_p.append(z)
	z = z * i
      pp.append(sub_p)
      for j in range(2*i, plim, i): qq.add(j)
    
  olis = [x for x in lis]
  for p in pp:
    if p[0] > B: break
    for q in p:
      (a, b) = solutions(q, N)
      if a == 0 and b == 0: continue
      print(q)
      for i in range(a-fr%q, len(lis), q):
	if i < 0: continue
	lis[i] = lis[i]/p[0]
      if a < b:
	for i in range(b-fr%q, len(lis), q):
	  if i < 0: continue
	  lis[i] = lis[i]/p[0]
      for i in range(len(lis)):
	print(str(fr+i)+": "+str(olis[i]) + " -> " + str(lis[i])) + ", ", 
      print("")
  for i in range(len(lis)):
    if(lis[i] == 1): 
	print(str(fr+i)+": "+str(olis[i]))

   
