# python 2.7.3
import sys
import math

[n, t, s] = map(int, sys.stdin.readline().split())
data = map(int, sys.stdin.readline().split())
for si in data:
	ans = t - abs(s - si) 
	isOdd = (ans % 2 == 1)
	ans = ans / 2 + max(s, si)
	
	if isOdd:
		tailStr = "500000"
	else:
		tailStr = "000000"
	
	print "%d.%s" % (ans, tailStr)

