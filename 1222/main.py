# python 2.7.3
import sys
import math

n = input()
if n <= 3:
    print n
elif n % 3 == 0:
    print 3 ** (n / 3)
elif n % 3 == 1:
    print 3 ** (n / 3 - 1) * 4
else:
    print 3 ** (n / 3) * 2

