# python 2.7.3
import sys
import math

n = 15
data = [0] * n
for i in range(n):
    data[i] = [None] * n
    for j in range(n):
        data[i][j] = 0

data[2][1] = 1
data[2][2] = 2
for row in range(2, 10):
    for col in range(1, row + 1):
        # 2 * col + 1
        data[row + 1][col] += data[row][col] * col
        data[row + 1][col + 1] += data[row][col] * (col + 1)
while True:
    m = input()
    if m == -1:
        break
    print sum(data[m])

    

