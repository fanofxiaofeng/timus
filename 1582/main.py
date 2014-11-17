# python 2.7.3
import sys
import math

data = sys.stdin.readline().split()
for i in range(len(data)):
    data[i] = float(data[i])

s = 0.0
for i in data:
    s += data[0] / i
x = 1000.0 / s
print int(round(x * data[0]))



    

