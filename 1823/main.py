# python 2.7.3
import sys
import math

[m0, mt, p] = map(int, sys.stdin.readline().split())
cnt = 0
p = 1 - 0.01 * p
lala = 1
while m0 * lala > mt:
    cnt += 1
    lala *= p
print cnt
    

