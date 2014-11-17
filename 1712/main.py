# python 2.7.3
import sys
import math

def readFourLine(a):
    for i in range(4):
        line = sys.stdin.readline()
        if line.endswith('\n'):
            a.append(line[:-1])
        else:
            a.append(line)

def transform(a):
    line = [0] * 4
    b = []
    for i in range(4):
        b.append(list(line))
   
    for row in range(4):
        for col in range(4):
            b[col][3 - row] = a[row][col]
    return b

board = []
readFourLine(board)
# print board

word = []
readFourLine(word)
# print word

s = ''
for i in range(4):
    for row in range(4):
        for col in range(4):
            if board[row][col] != '.':
                s += word[row][col]
    board = transform(board)
    # print board
print s

    

