# python 2.7.3
import sys
import math

[n, x] = sys.stdin.readline().split()

n = int(n)
x = int(x)

data = sys.stdin.readline().split()
for i in range(len(data)):
    data[i] = int(data[i])

left_nearest = 2000
right_nearest = 2000
r = ['ob', 'ob']

if x > 0:
    right_nearest = x
    r[1] = 'ex'
else:
    left_nearest = -x
    r[0] = 'ex'

for i in data:
    if i > 0:
        if i < right_nearest:
            right_nearest = i
            r[1] = 'ob'
    else:
        if abs(i) < left_nearest:
            left_nearest = abs(i)
            r[0] = 'ob'

ans = ''
if r[1] == 'ex':
    ans += str(right_nearest) + ' '
else:
    if r[0] == 'ob':
        pass
    else:
        ans += str(2 * right_nearest + left_nearest) + ' '

if r[0] == 'ex':
    ans += str(left_nearest)
else:
    if r[1] == 'ob':
        ans += 'Impossible'
    else:
        ans += str(2 * left_nearest + right_nearest)
print ans

    

