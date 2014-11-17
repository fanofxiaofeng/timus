# python 2.7.3
import sys
import math

def f(i, n, m):
    if n == 0:
        return 1 % m
    temp = f(i, n / 2, m)
    if n % 2 == 0:
        return (temp ** 2) % m
    else:
        return (temp ** 2 * i) % m

[n, m, y] = sys.stdin.readline().split()
n = int(n)
m = int(m)
y = int(y)

s = ''
for i in range(m):
    # print 'f(%d, %d, %d) = %d' % (i, n, m, f(i, n, m))
    if f(i, n, m) == y % m:
        if s:
            s += ' '
        s += str(i)
        
if s:
    print s
else:
    print -1


    

