#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_D

n = int(input())
r = [int(input()) for i in range(n)]

minv = 10**10
maxv = -(10**10)
for i in r:
    maxv = max(maxv, i - minv)
    if i < minv:
        minv = i
print(maxv)
