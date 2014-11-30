# python 2.7.3
import sys
import math

N = input()
factors = [2, 3, 5, 7]
cnt = [0 for i in factors]

if N == 0:
	print '10'
	sys.exit(0)
if N == 1:
	print '1'
	sys.exit(0)

for factor in factors:
	while N % factor ==  0:
		cnt[factors.index(factor)] += 1
		N /= factor
if N != 1:
	print -1
	sys.exit(0)

result = []
result.extend(['5'] * cnt[factors.index(5)])
result.extend(['7'] * cnt[factors.index(7)])

result.extend(['9'] * (cnt[factors.index(3)] / 2))
result.extend(['8'] * (cnt[factors.index(2)] / 3))

remain = cnt[factors.index(2)] % 3
if cnt[factors.index(3)] % 2 == 0:        
        if remain == 1:
                result.append('2')
        elif remain == 2:
                result.append('4')
else:
        if remain == 0:
                result.extend(['3'])
        elif remain == 1:
                result.extend(['6'])
        elif remain == 2:
                result.extend(['2', '6'])
result.sort()
print ''.join(result)
		
		






