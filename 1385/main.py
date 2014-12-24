# python 2.7.3
import sys
import math

n = input()
if n == 1:
	print 14
elif n == 2:
	print 155
else:
	a = '1575' + '0' * (n - 3)
