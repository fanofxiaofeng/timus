# python 2.7.3
import sys
import math
from collections import deque

def isValid(pos, n):
	return (0 <= pos[0] < n) and (0 <= pos[1] < n)

def new(pos, visited):
	return not visited[pos[0]][pos[1]]

deltas = [[-1, 0], [0, -1], [0, 1], [1, 0]]

n = input()
data = [0 for i in range(n * n)]
for i in range(n * n):
	data[i] = input()
data.sort()
data = data[::-1]

visited = [[False for col in range(n)] for row in range(n)]
out = [[0 for col in range(n)] for row in range(n)]
start = [n / 2, n / 2]
visited[start[0]][start[1]] = True
out[start[0]][start[1]] = data[0]
cnt = 0
d = deque()
d.append(start)
while d:
	head = d.popleft()
	for delta in deltas:
		temp = [head[0] + delta[0], head[1] + delta[1]]		
		if isValid(temp, n) and new(temp, visited):
			cnt += 1
			visited[temp[0]][temp[1]] = True
			out[temp[0]][temp[1]] = data[cnt]
			d.append(temp)
for row in out:
        print ' '.join(map(str, row))



	
