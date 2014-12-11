# python 2.7.3
import sys
import math

n = input()
nStr = str(n)

cnt = [0 for i in range(10)]

common = 0
for pos in range(len(nStr)):
	value = int(nStr[pos])
	width = len(nStr) - 1 - pos
	common += 10 ** width * width / 10 * (value)
	for i in range(value):
		cnt[i] += 10 ** width

	if pos + 1 == len(nStr):		
		cnt[value] += 1 
	else:
		cnt[value] += 1 + int(nStr[(pos + 1):])
for pos in range(len(cnt)):
	cnt[pos] += common

cnt[0] -= int('1' * len(nStr))
for i in cnt:
	print i


# For example, try to figure out what you will do when it is 2014
# To simplify, we add heading 0's (we will deal with them in the end)
# 0000
# 0001
# ....
# 1000
# 1001
# 1002
# ....
# 1999
# 2000
# 2001
# ....
# 2013
# 2014
# Then, you will find out the way to solve the problem.
