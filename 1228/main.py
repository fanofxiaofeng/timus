# python 2.7.3
import sys
import math

[n, s] = map(int, sys.stdin.readline().split())

data = [0 for i in range(n)]

for i in range(n):
    data[i] = input()

value = [s / data[0] - 1]

for i in range(n - 1):
    value.append(data[i] / data[i + 1] - 1)

for i in range(len(value)):
    value[i] = str(value[i])

print ' '.join(value)
