# python 2.7.3
import sys
import math
import copy

def dfs(newData, color, visited, i):	
	cur = color[i]
	for j in newData[i]:
		if color[j] == cur:
			return False
		else:
			if not visited[j]:
				color[j] = 1 - cur			
				visited[j] = True
				judge = dfs(newData, color, visited, j)
				if not judge:
					return False
	return True

def DFS(newData, color, visited):
	for i in range(1, len(newData)):
		if color[i] == -1:
			color[i] = 0
		visited[i] = True
		judge = dfs(newData, color, visited, i)
		if not judge:
			return False
	return True

n = input()
data = [None for i in range(n + 1)]
color = [-1 for i in range(n + 1)]
visited = [False for i in range(n + 1)]
for i in range(1, n + 1):
	data[i] = map(int, sys.stdin.readline().split())[:-1]
	
newData = copy.deepcopy(data)
for small in range(1, n + 1):		
	for big in data[small]:
		newData[big].append(small)

judge = DFS(newData, color, visited)
if not judge:
	print -1
else:
	print ''.join(map(str, color[1:]))
