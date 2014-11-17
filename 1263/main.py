# python 2.7.3
import sys
import math

n, m = sys.stdin.readline().split()

m = int(m)
n = int(n)

cnt = [0] * n

for i in range(m):
    num = input()
    cnt[num - 1] += 1

for i in range(n):
    print "%.2f%%" % (float(cnt[i]) / m * 100)
    
