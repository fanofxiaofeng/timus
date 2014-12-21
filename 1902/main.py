# python 2.7.3
import sys
import math

[n, t, s] = map(int, sys.stdin.readline().split())
data = map(int, sys.stdin.readline().split())
for si in data:
	len = n - abs(s - si) / float(t) * n
	ans = len / 2.0 / n * t + max(s, si) 
	print "%.6f" % ans

