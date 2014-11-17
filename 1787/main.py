# python 2.7.3
import sys
import math

[k, n] = sys.stdin.readline().split()
k = int(k)
n = int(n)
data = sys.stdin.readline().split()

for i in range(n):
    data[i] = int(data[i])

cnt = 0
for i in range(n):
    cnt += data[i]
    delta = min(cnt, k)
    cnt -= delta

print cnt

    

