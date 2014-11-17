# python 2.7.3
import sys
import math

n = 3
a = [0] * n
b = [0] * n
for i in range(n):
    a[i], b[i] = sys.stdin.readline().split()
    a[i] = int(a[i])
    b[i] = int(b[i])

print a[0] - a[2], b[0] - b[1]
