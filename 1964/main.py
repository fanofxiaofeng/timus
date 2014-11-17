# python 2.7.3
import sys
import math

n, k = map(int, sys.stdin.readline().split())
a = map(int, sys.stdin.readline().split())

others = 0

for i in a:
    if i > others:
        qualified = i - others
        others = n - qualified
    else:
        qualified = 0
        break
print qualified
    
    
