# python 2.7.3
import sys
import math

n = input()
s_bound = 10
h_bound = 2

ok = True

for i in range(n):
    [num, state] = sys.stdin.readline().split()
    num = int(num)
    if state == 'hungry':
        if num >= s_bound:
            ok = False
            break
        else:
            h_bound = max(h_bound, num)
    else:
        if num <= h_bound:
            ok = False
            break
        else:
            s_bound = min(s_bound, num)

if ok:
    print s_bound
else:
    print 'Inconsistent'
    


    

