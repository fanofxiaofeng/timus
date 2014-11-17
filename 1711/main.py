# python 2.7.3
import sys
import math

n = input()
data = []
q = []
for i in range(n):
    line = raw_input()
    words = line.split()
    words.sort()
    data.append(words)
    q.extend(words)
# print data
# print q

q.sort()
order = sys.stdin.readline().split()
for i in range(n):
    order[i] = int(order[i]) - 1

possible = True
pos = 0
result = []
for i in order:
    found = False
    for word in data[i]:
        r = q.index(word)
        if r >= pos:
            result.append(word)
            pos = r + 1
            found = True
            break
    if not found:
        possible = False
        break
if possible:
    for i in result:
        print i
else:
    print 'IMPOSSIBLE'
    


    

