# python 2.7.3
import sys
import math

def f(n):
	level = n / 2
	print level * (level + 1) / 2
	for i in range(1, level + 1):
		if i % 2 == 0:
			continue
		left, right = 2 * i - 1, 2 * i
		print "%d %d" % (left, right)
		for j in range(i + 1, level + 1):
			print "%d %d" % (left, 2 * j)
			print "%d %d" % (right, 2 * j - 1)	

n = input()

f(n)
