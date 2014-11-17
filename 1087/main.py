# python 2.7.3
import sys
import math

[n, m] = map(int, sys.stdin.readline().split())
data = map(int, sys.stdin.readline().split())

judge = ['p'] * (n + 1)
judge[0] = 'n'

for i in range(1, len(judge)):    
    for j in data:
        if i >= j and judge[i - j] == 'p':
            judge[i] = 'n'
            break
if judge[n] == 'n':
    print 1
else:
    print 2
