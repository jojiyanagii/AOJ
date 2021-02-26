#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_B

N = int(input())
somelist = list(map(int, input().split()))
count = 0
for i in range(N):
    min_index = i 
    for j in range(i + 1, N):
      if somelist[min_index] > somelist[j]:
        min_index = j 
    if i != min_index:
      x = somelist[i]
      somelist[i] = somelist[min_index]
      somelist[min_index] = x
      count += 1

print(*somelist)
print(count)

