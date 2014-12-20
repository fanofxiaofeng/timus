# python 2.7.3
import sys
import math

_ = input()
data = map(int, sys.stdin.readline().split())

max = 0

for i in data:
	if i > max + 1:
		break
	else:
		max += i
print max + 1
