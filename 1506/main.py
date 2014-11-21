# python 2.7.3
import sys
import math

[n, k] = map(int, sys.stdin.readline().split())

data = map(int, sys.stdin.readline().split())

if n % k == 0:
    row = n / k
else:
    row = n / k + 1

matrix = [[-1 for j in range(k)] for i in range(row)]
for i in range(len(data)):
    matrix[i % row][i / row] = data[i]

col = k
for r in range(row):
    result = ''
    for c in range(col):
        if matrix[r][c] != -1:
            result += "%4d" % matrix[r][c]
    print result
    



    

