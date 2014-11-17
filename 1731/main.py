# python 2.7.3
import sys
import math

n, m = map(int, sys.stdin.readline().split())
l1 = range(1, n + 1)
l2 = range(1, m + 1)
l2 = map(lambda x, y: x * y, [100] * len(l2), l2)
print ' '.join(map(str, l1))
print ' '.join(map(str, l2))
    

