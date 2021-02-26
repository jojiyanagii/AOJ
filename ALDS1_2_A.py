#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_A

N = int(input())
A = list(map(int, input().split()))

flag = 1
i = 0
num_change = 0
while flag:   
  flag = 0
  for j in range(N-1, i, -1):
    if A[j] < A[j-1]:
      A[j], A[j-1] = A[j-1], A[j]
      num_change += 1
      flag = 1
  i += 1
print(' '.join(str(i) for i in A))
print(num_change)

