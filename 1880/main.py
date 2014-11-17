# python 2.7.3
import sys
import math

_ = input()
d1 = map(int, sys.stdin.readline().split())
s1 = set(d1)

while True:
    try:
        _ = input()
        d2 = map(int, sys.stdin.readline().split())
        s2 = set(d2)
        s1 = s1.intersection(s2)
    except:
        break
print len(s1)

    

