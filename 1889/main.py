# python 2.7.3
import sys
import math

n = input()
words = [None for i in range(n)]
for i in range(n):
	words[i] = raw_input()

ans = []
for i in range(1, n + 1):
	if n % i != 0:
		continue
	q = n / i
	lan = set()
	valid = True
	for j in range(q):
		temp = set(words[j * i:(j + 1) * i])
		if 'unknown' in temp:
			temp.remove('unknown')
		if len(temp) > 1:
			valid = False
			break
		if len(temp) == 1:
			if list(temp)[0] in lan:
				valid = False
				break
			else:
				lan.add(list(temp)[0])
		else:
			continue
	if valid:
		ans.append(q)
if not ans:
	print 'Igor is wrong.'
else:
	print ' '.join(map(str, ans[::-1]))
