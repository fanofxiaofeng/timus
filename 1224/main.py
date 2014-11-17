# python 3.4.0
import sys
import math

n, m = sys.stdin.readline().split()

m = int(m)
n = int(n)

if m >= n:
    print(2 * (n - 1))
else:
    print(2 * (m - 1) + 1)
