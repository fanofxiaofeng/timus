# python 2.7.3
import sys
import math

[n1, c1] = map(int, sys.stdin.readline().split())
[n2, t, c2] = map(int, sys.stdin.readline().split())
[n3] = map(int, sys.stdin.readline().split())

k = input()
total = 0
for i in range(k):
    data = raw_input()
    [mm, ss] = map(int, data.split(':'))
    if mm == 0 and ss <= 6:
        continue
    elif ss != 0:
        mm += 1
    total += mm

print "Basic:     %d" % (n1 + c1 * total)
if total > t:
    temp = total - t
else:
    temp = 0
print "Combined:  %d" % (n2 + c2 * temp)
print "Unlimited: %d" % n3

    

