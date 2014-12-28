# python 2.7.3
import sys
import math

[n, m, p] = map(int, sys.stdin.readline().split())

m = {}
for i in range(n):
	s = raw_input()
	for c in s:
		m[c] = m.get(c, 0) + 1

for i in range(p):
	s = raw_input()
	for c in s:
		m[c] = m.get(c, 0) - 1

ans = []
for i, v in m.items():	
	ans.extend(i * v)
ans.sort()

print ''.join(ans)

