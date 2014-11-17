# python 2.7.3
import sys
import math

num = sys.stdin.readline()
num = int(num)

d = {}

for i in range(num):
    temp = sys.stdin.readline()
    if temp.endswith('\n'):
        line = temp[:-1]
    else:
        line = temp
    # print line
    if line in d:
        d[line] += 1
    else:
        d[line] = 1
    
for k, v in d.iteritems():
    if v >= 2:
        print k

    

