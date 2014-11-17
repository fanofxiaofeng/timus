# python 2.7.3
import sys
import math



def choose(fac, n, k):
    assert(n >= k)
    return fac[n] / fac[k] / fac[n - k]
    


fac = [1] * 25
for i in range(1, 25):
    fac[i] = fac[i - 1] * i
# print fac
# print choose(fac, 10, 2)
n = input()
if n == 1:
    print 0
elif n == 2:
    print 2
else:
    cnt = 0
    for j in range(2, n + 1):
        cnt += choose(fac, n, j) * fac[j]
    print cnt
        
    


    

