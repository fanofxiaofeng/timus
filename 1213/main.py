# python 3.4.0
import sys
import math

names = set()
# print s

while True:
    s = raw_input().split('-')
    if len(s) == 1 and s[0] == '#':
        break
    for i in s:
        names.add(i)
print len(names) - 1
    
    
