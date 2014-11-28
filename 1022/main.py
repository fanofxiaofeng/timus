# python 2.7.3
import sys
import math

def dfs(data, color, result, time, stack, i):	
	stack.append(i)
	color[i] = 'gray'
	for j in data[i]:
		if color[j - 1] == 'white':
			dfs(data, color, result, time, stack, j - 1)
	time[0] += 1
	color[i] = 'black'
	result.append(i)
	stack.pop()

def DFS(data, color, result, time):
	stack = []
	for i in range(len(data)):
		if color[i] == 'white':
			dfs(data, color, result, time, stack, i)

n = input()
data = [[] for i in range(n)]
color = ['white' for i in data]
result = [] 
time = [0]

for i in range(n):
	temp = map(int, raw_input().split())[:-1]	
	data[i] = temp

DFS(data, color, result, time)
out = map(lambda x: str(x + 1), result)
print ' '.join(out[::-1])
