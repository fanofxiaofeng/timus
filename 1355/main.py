# python 2.7.3
import sys
import math

def calc(a, b):
	if b % a != 0:
		return -1
	n = b / a
	cnt = 0
	i = 2
	while True:
		if n == 1:
			break
		if i * i > n:
			# n is prime
			cnt += 1
			break
		if n % i == 0:
			while n % i == 0:
				n /= i
				cnt += 1
		i += 1
	return cnt

n = input()
for i in range(n):
	[a, b] = map(int, sys.stdin.readline().split())
	print calc(a, b) + 1
