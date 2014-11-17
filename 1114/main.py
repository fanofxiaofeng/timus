# python 2.7.3
import sys
import math

fac = [1 for i in range(40)]
for i in range(1, len(fac)):
    fac[i] = fac[i - 1] * i


def choose(n, k):
    global fac    
    return fac[n] / fac[k] / fac[n - k]

def calc(box, ball):
    result = 0
    for i in range(ball + 1):
        result += choose(box - 1 + i, i)
        # print result
    return result

[n, a, b] = map(int, sys.stdin.readline().split())
print calc(n, a) * calc(n, b)





    

