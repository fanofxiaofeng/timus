# -*- coding: utf-8 -*-
# python 2.7.3
import sys
import math

n = input()

score1 = map(int, sys.stdin.readline().split())
score2 = map(int, sys.stdin.readline().split())

data1 = [[] for i in range(6 + 1)]
data2 = [[] for i in range(6 + 1)]

for pos in range(len(score1)):
	value = score1[pos]
	data1[value].append(pos + 1)
	value = score2[pos]
	data2[value].append(pos + 1)
# print data1
# print data2
total1 = sum(score1)
total2 = sum(score2)

if total1 >= total2:
	result1 = reduce(lambda x, y: x + y, data1)
	result2 = reduce(lambda x, y: x + y, data2[::-1])
else:
	result1 = reduce(lambda x, y: x + y, data1[::-1])
	result2 = reduce(lambda x, y: x + y, data2)

for pos in range(len(result1)):
	print "%d %d" % (result1[pos], result2[pos])
	
	


