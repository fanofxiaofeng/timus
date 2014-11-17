# python 2.7.3
import sys
import math

n = input()

m = {}
m['A'] = 1
m['O'] = 1
m['P'] = 1
m['R'] = 1

m['B'] = 2
m['M'] = 2
m['S'] = 2

pos = 1
cnt = 0
for i in range(n):
    name = raw_input()
    c = name[0]
    if c in m:
        cnt += abs(pos - m[c])
        pos = m[c]
    else:
        cnt += abs(pos - 3)
        pos = 3
print cnt
    


    
