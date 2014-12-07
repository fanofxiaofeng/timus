# python 2.7.3
import sys
import math

class Member:
    def __init__(self, num):
        self.num = num
        self.group = 0

    def setGroup(self, g):
        self.group = g

    def getGroup(self):
        return self.group

    def getNum(self):
        return self.num

n = input()

data = [None for i in range(n + 1)]
for i in range(n + 1):
    data[i] = Member(i)

for i in range(1, n + 1):
    line = map(int, sys.stdin.readline().split())
    line.pop()  # remove the trailing 0
    
    if data[i].getGroup() != 0:
        continue

    found = False
    for j in line:
        if not found:
            if data[j].getGroup() != 0:
                found = True                
                data[i].setGroup(3 - data[j].getGroup())
        else:
            if data[j].getGroup() == 0:
                data[j].setGroup(3 - data[i].getGroup())
    if not found:
        data[i].setGroup(1)
        for j in line:
            data[j].setGroup(2)

store = filter(lambda x: x.getNum() != 0 and x.getGroup() == 1, data)
result = map(lambda x: str(x.getNum()), store)
print len(result)
print ' '.join(result)
