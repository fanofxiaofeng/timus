# python 2.7.3
import sys
import math

[m, d1, d2] = map(int, sys.stdin.readline().split())
workload = m * d1
# print 'workload is: %d' % workload

if workload % d2 == 0:    
    n = workload / d2
else:
    n = workload / d2 + 1

for i in range(d2):
    if workload >= n:
        print str(n),
    else:
        print str(workload),
    workload = max(workload - n, 0)
    

    

