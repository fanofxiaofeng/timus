# python 2.7.3
import sys
import math

def f(x, y, c):
    xlow = 0
    xhigh = x
    while True:
        xmid = (xlow + xhigh) / 2
        if c >= xmid and c <= xmid + y:
            break
        elif c < xmid:
            xhigh = xmid - 1
        else:
            xlow = xmid + 1
    return [xmid, c - xmid]

x, y, c = sys.stdin.readline().split()
x, y, c = int(x), int(y), int(c)
if x + y < c:
    print 'Impossible'
else:
    result = f(x, y, c)
    print "%d %d" % (result[0], result[1])
    


    
