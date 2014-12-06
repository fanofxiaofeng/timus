# python 2.7.3
import sys
import math

data = [0 for i in range(55)]
data[1] = 1
for i in range(2, len(data)):
    data[i] = 2 * data[i - 1]

n = input()
pos = raw_input()

cnt = 0

remainPos = 'A'
for i in range(len(pos), 0, -1):
    currentPos = pos[i - 1]
    if remainPos == currentPos:
        continue
    temp = ['A', 'B', 'C']
    temp.remove(currentPos)
    temp.remove(remainPos)
    remainPos = temp[0]
    cnt += data[i]
print cnt       
