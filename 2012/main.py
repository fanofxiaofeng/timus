# python 2.7.3
import sys
import math

f = input()
required = (12 - f) * 45 / 60  + 1 + (((12 - f) * 45) % 60 != 0)
if required <= 5:
    print 'YES'
else:
    print 'NO'


    
