# python 2.7.3
import sys
import math

n, k = sys.stdin.readline().split()
n = int(n)
k = int(k)

data = sys.stdin.readline().split()
for i in range(len(data)):
    data[i] = int(data[i])

a = 0
b = 0

for i in range(len(data)):
    if data[i] > k:
        a += data[i] - k
    else:
        b += k - data[i]

print a, b
