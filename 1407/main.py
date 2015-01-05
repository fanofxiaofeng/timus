# python 2.7.3
import sys
import math

n = input()
a = 2

for i in range(2, n + 1):
	if a % (2 ** i) == 0:
		a += 2 * 10 ** (i - 1)
	else:
		a += 10 ** (i - 1)
	
print a
