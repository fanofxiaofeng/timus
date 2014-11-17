# python 2.7.3
import sys
import math

n = input()
k = math.trunc(math.sqrt(2 * n))

for i in range(k, 0, -1):
    remain = n - i * (1 + i) / 2
    if remain >= 0 and remain % i == 0:
        print remain / i + 1, i
        break

    

