# python 2.7.3
import sys
import math

data = [[None] for row in range(5 + 1)]

for row in range(1, 5 + 1):
	data[row].extend(map(int, sys.stdin.readline().split()))

temp = [2, 3, 4]
opt = 10000 * 10000

for i in temp:
	for j in temp:
		for k in temp:
			if i == j or i == k or j == k or k == 3:
				continue
			s = data[1][i] + data[i][j] + data[j][k] + data[k][5]
			if s < opt:				
				opt = s
				record = [1, i, j, k, 5]
print opt
print ' '.join(map(str, record))

