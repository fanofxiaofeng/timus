# python 2.7.3
import sys
import math

[n, k] = map(int, sys.stdin.readline().split())
l = k - 1
r = n - k
if max(l, r) >= 2:
    print max(l, r) - 2
else:
    print 0
    

