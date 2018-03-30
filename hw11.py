from ec import E

def test(a, p): 
  E.params(a, -a, p)
  s = set()
  e = E(1, 1) + E(1, 1)

  cnt = 1
  while e.P != (1, 1):
    e = e + E(1, 1)
    cnt = cnt + 1
  print(cnt)

if __name__ == '__main__':
  test(865095, 1000003)
