# python 2.7.3
import sys
import math
from collections import deque

def first2second(n, magic):
    isBlack = [[False for x in range(magic)] for y in range(magic)]
    leftmost, lowest = magic, magic
    for i in range(n):
        [x, y] = map(int, sys.stdin.readline().split())
        isBlack[x][y] = True
        if x < leftmost:
            leftmost = x
            if y < lowest:
                lowest = y

    dq = deque()
    dq.append((leftmost, lowest))
    isBlack[leftmost][lowest] = False
    info = 'RTLB'
    Delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    print leftmost, lowest
    while True:
        current = dq.popleft()
        # print 'current is:', current
        neighbour = ''
        for delta in Delta:
            [xtemp, ytemp] = map(lambda a, b: a + b, current, delta)
            if isBlack[xtemp][ytemp] == True:
                neighbour += info[Delta.index(delta)]
                dq.append([xtemp, ytemp])
                isBlack[xtemp][ytemp] = False
        if len(dq) != 0:
            print neighbour + ','
        else:
            print '.'
            break

def seconde2first(data, magic):
    isBlack = [[False for x in range(magic)] for y in range(magic)]
    isBlack[data[0]][data[1]] = True
    dq = deque()
    dq.append(tuple(data))
    info = 'RTLB'
    Delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while True:
        message = raw_input()
        current = dq.popleft()
        if message[:-1]:
            for ch in message[:-1]:
                delta = Delta[info.index(ch)]
                [xtemp, ytemp] = map(lambda a, b: a + b, current, delta)
                isBlack[xtemp][ytemp] = True
                dq.append((xtemp, ytemp))
        if message[-1] == '.':
            break
    cnt = 0
    for x in range(magic):
        for y in range(magic):
            if isBlack[x][y]:
                cnt += 1
    print cnt
    for x in range(magic):
        for y in range(magic):
            if isBlack[x][y]:
                print x, y




magic = 15
data = map(int, sys.stdin.readline().split())
if len(data) == 1:
    first2second(data[0], magic)
else:
    seconde2first(data, magic)



