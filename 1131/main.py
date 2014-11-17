# python 2.7.3
import sys
import math

[n, k] = sys.stdin.readline().split()
n = int(n)
k = int(k)
# print 'n: %d, k: %d' % (n, k)

t = 0
cnt = 1
while cnt < n:
    if cnt <= k:
        # print 'if branch'
        cnt *= 2
        t += 1
    else:
        # print 'else branch'    
        # print (n - cnt) / k
        t += (n - cnt) / k + ((n - cnt) % k != 0)
        break
print t
    
    



    

