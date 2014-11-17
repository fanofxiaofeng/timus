# python 2.7.3
import sys
import math

num = sys.stdin.readline()
num = int(num)

s = set()

cnt = 0
for i in range(num):
    brandtemp = sys.stdin.readline()
    if brandtemp.endswith('\n'):
        brand = brandtemp[:-1]
    else:
        brand = brandtemp

    if brand in s:
        cnt += 1
    else:
        s.add(brand)
print cnt

    

