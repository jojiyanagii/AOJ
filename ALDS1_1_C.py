#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_C

import math
N = int(input())
A = []

def isprime(x):
  if x == 2:
    return True
  if x < 2 or x % 2 == 0:
    return False
  i = 3
  while i <= math.sqrt(x):
    if x % i == 0:
      return False
    i = i + 2
  return True

count = 0

for _ in range(N):
  A.append(int(input()))
  if isprime(A[_]) == True:
    count += 1
print(count)

