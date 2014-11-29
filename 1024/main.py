# python 2.7.3
import sys
import math

def gcd(a, b):
	# assume a and b are both non-negative and a ** 2 + b ** 2 > 0
	if not a or not b:
		return a + b
	else:
		return gcd(b, a % b)

def calc(li):
	if len(li) == 1:
		return li[-1]
	v1 = li.pop()
	v2 = li.pop()
	temp = v1 * v2 / gcd(v1, v2)
	while li:
		new = li.pop()
		temp = new * temp / gcd(new, temp)
	return temp
	

N = input()
data = map(int, sys.stdin.readline().split())
data = map(lambda x: x - 1, data)

# print data

record = []
appeared = [False for i in range(N)]
for i in range(N):
	if not appeared[i]:
		temp = [i]
		while data[temp[-1]] != temp[0]:
			temp.append(data[temp[-1]])					
		record.append(len(temp))
		for j in temp:
			appeared[j] = True
# print record
print calc(record)
