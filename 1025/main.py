# python 2.7.3
import sys
import math


k = input()
data = sys.stdin.readline().split()

for i in range(len(data)):
    data[i] = int(data[i])

data.sort()

cnt = 0
for pos in range((k + 1) / 2):    
    cnt += (data[pos] + 1) / 2

print cnt
