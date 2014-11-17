# python 2.7.3
import sys
import math

num = sys.stdin.readline()
num = int(num)

d = {}

for i in range(num):
    line = sys.stdin.readline()[:-1]
    # print line
    if line in d:
        d[line] += 1
    else:
        d[line] = 1
    
opt = 0
out = ""
for k, v in d.iteritems():
    if v > opt:
        out = k
        opt = v
print out
    

