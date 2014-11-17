# -*- coding: utf-8 -*-
# python 2.7.3
import sys
import math
from collections import deque

m = 10 ** 9 + 7

[n, a, b] = map(int, sys.stdin.readline().split())

atail = deque([0 for i in range(a)]) # 统计各种以1结尾的情形个数
btail = deque([0 for i in range(b)]) # 统计各种以2结尾的情形个数

atail.popleft()
atail.appendleft(1)
btail.popleft()
btail.appendleft(1)

asum = 1 # 记录atail数组中所有元素的和
bsum = 1 # 记录btail数组中所有元素的和

# print atail
# print btail

for i in range(n - 1):
    alast = atail.pop()
    atemp = (asum - alast) % m
    
    blast = btail.pop()
    btemp = (bsum - blast) % m
    
    atail.appendleft(bsum)
    btail.appendleft(asum)

    asum, bsum = (atemp + bsum) % m, (btemp + asum) % m
result = (asum + bsum) % m
print result
 
