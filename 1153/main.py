# python 2.7.3
import sys
import math

f = lambda x: (1 + x) * x / 2

n = input()

low = 1
high = 1
while f(high) < n:
	high *= 2

while low <= high:
	mid = (low + high) / 2
	v = f(mid)
	if v == n:
		print mid
		break
	elif v < n:
		low = mid + 1
	else:
		high = mid - 1
