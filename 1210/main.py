# python 2.7.3
import sys
import math

INF = 100000000

n = input()
dataRecord = [None for i in range(n + 1)]
isReachable = [None for i in range(n + 1)]

dataRecord[0] = [0, 0]
isReachable[0] = [False, True]

for i in range(1, n + 1):
    ki = input()    
    isReachable[i] = [False for j in range(ki + 1)]
    dataRecord[i] = [INF for j in range(ki + 1)]

    for j in range(1, ki + 1):
        data = map(int, sys.stdin.readline().split())
        data.pop() # remove the trailing zero which is just a symbol
        pre = i - 1

        for pos in range(0, len(data), 2):
            start = data[pos]            
            if isReachable[pre][start]:
                isReachable[i][j] = True
                break

        if isReachable[i][j]:
            for pos in range(0, len(data), 2):
                start = data[pos]
                delta = data[pos + 1]
                if isReachable[pre][start]:
                    temp = dataRecord[pre][start] + delta
                    if temp < dataRecord[i][j]:
                        dataRecord[i][j] = temp

    if i != n:  # if not the highest level, then read the star line
        star = raw_input()
print min(dataRecord[n])          
        

    
    
