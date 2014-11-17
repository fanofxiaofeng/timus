# python 2.7.3
import sys
import math

n = input()
m = {}
for i in range(n):
    num = input()
    if num in m:
        m[num] += 1
    else:
        m[num] = 1

cnt = 0
for k, v in m.iteritems():
    if v >= 4:
        cnt += v / 4

print cnt

    

