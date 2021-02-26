#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_C

import copy
N = int(input())
C = list(input().split())
D = copy.deepcopy(C)

#bubble_sort(C, N)
for i in range(N):
  for j in range(N-1, i, -1):
    if C[j-1][1] > C[j][1]:
      C[j], C[j-1] = C[j-1], C[j]
print(*C)
print("Stable")
  
#selection_sort(C,N)
for i in range(0, N):
  min_index = i
  for j in range(i+1, N):
    if D[min_index][1] > D[j][1]:
      min_index = j
  x = D[i]
  D[i] = D[min_index]
  D[min_index] = x
  #D[i], D[min_index] = D[min_index], D[i]

print(*D)
if C == D:
  print("Stable")
else:
  print("Not stable")

