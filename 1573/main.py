# python 2.7.3
import sys
import math

[b, r, y] = map(int, sys.stdin.readline().split())
k = input()
cnt = 1
for i in range(k):
    color = raw_input()
    if color == 'Blue':
        cnt *= b
    elif color == 'Red':
        cnt *= r
    else:
        cnt *= y
print cnt


    

