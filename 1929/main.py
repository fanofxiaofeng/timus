# python 2.7.3
import sys
import math

n, m = map(int, sys.stdin.readline().split())

data = map(int, sys.stdin.readline().split())

qualified = (1 in data)


if m < n / 3:
	# impossible
	result = 0
elif m == n / 3:
	if qualified:
		others = n - m
		result = others * (others - 1) / 2
	else:		
		others = n - m - 1
		result = m * others
elif m == n / 3 + 1:
	if qualified:
		others = n - m
		result = others * (others - 1) / 2 + (m - 1) * others
	else:
		others = n - m - 1
		result = m * others + m * (m - 1) / 2
else:
	if qualified:
		result = (n - 1) * (n - 1 - 1) / 2
	else:
		others = n - m - 1
		result = (n - 1) * (n - 1 - 1) / 2 - others * (others - 1) / 2
print result

