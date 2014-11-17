# python 2.7.3
import sys
import math

[n, m] = sys.stdin.readline().split()
n = int(n)
m = int(m)

target = 3 * n

cur = 0
cnt = 0
for i in range(m):
    temp = input()
    cnt += 1
    cur += temp
    if cur > target:
        print 'Free after %d times.' % cnt
        break
else:
    print 'Team.GOV!'
    


    

