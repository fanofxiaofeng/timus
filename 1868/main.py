# python 2.7.3
import sys
import math

m = {}
for i in range(4):
	gold = raw_input()
	m[gold] = "gold"
for i in range(4):
	silver = raw_input()
	m[silver] = "silver"
for i in range(4):
	bronze = raw_input()
	m[bronze] = "bronze"

ans = [0 for i in range(12 + 1)]
n = input()
for i in range(n):
	k = input()
	cnt = 0
	for j in range(k):
		[name, colon, medal] = raw_input().split()
		if name in m:
			if m[name] == medal:
				cnt += 1
	ans[cnt] += 1

pos = 12
while True:
	if ans[pos] != 0:
		print ans[pos] * 5
		break
	pos -= 1
		
	


