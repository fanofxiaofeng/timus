# python 2.7.3
import sys
import math

def addto(a, b, shift):
    for i in range(len(a)):
        b[i + shift] += a[i]

def init():
    result = [[1]]
    for i in range(60):
        temp = [0 for i in range(len(result[-1]) + 9)]
        # print len(temp)
        for j in range(10):
            addto(result[-1], temp, j)
        result.append(temp)
    return result
        
        
[n, s] = map(int, sys.stdin.readline().split())
result = init()
if s % 2 == 1:
    print 0
elif s / 2 > 9 * n:
    print 0
else:
    # print result[n]
    temp = result[n][s / 2]
    print temp ** 2


