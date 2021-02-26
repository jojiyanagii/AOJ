#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_B

a, b = map(int, input().split())

def gcd(x,y):
  if x < y:
    x, y = y, x
  while y > 0:
    r = x % y
    x = y
    y = r
  return x

print(gcd(a, b))

