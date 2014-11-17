# python 2.7.3
import sys
import math

n, m = sys.stdin.readline().split()
n = int(n)
m = int(m)
if n * m % 2 == 0:
    print "[:=[first]"
else:
    print "[second]=:]"

    

