# python 2.7.3
import sys
import math

ans = [0] * 10

def f(s):
    s = str(s)
    r = 0
    for c in s:
        r += int(c)
    return r

for i in range(1, 10):
    if i % 2 == 0:
        m = {}
        for j in range(100):
            m[j] = 0
        for j in range(10 ** (i / 2)):
            m[f(j)] += 1
        cnt = 0
        for k, v in m.iteritems():
            cnt += v ** 2
        ans[i] = cnt
    else:
        ans[i] = 10 * ans[i - 1]
# print ans

k = input()
print ans[k]
    
