# python 2.7.3
import sys
import math

def h(li):
    while li:
        print li[0],
        li.pop(0)

def g(n):
    if n in [0, 1, 8]:
        return str(n)
    elif n in [6, 9]:
        return str(15 - n)
    else:
        return '-'

def f(n):
    high = n / 10
    low = n % 10
    return g(low) + g(high)

result = []
for i in range(1, 100):
    result.append(f(i))
# print len(result)
result.append('--')

start = 0
record = [-1, -1]
opt = -1
acc = 0
for i in range(100):
    if '-' in result[i]:
        if acc > opt:
            record = [i - acc, i]
            opt = acc
        acc = 0
    else:
        acc += 1
# print record
# print opt
# print result
lala = result[record[0]: record[1]]
lala = lala[::-1]
        
n = input()
if n > 4:
    print 'Glupenky Pierre'
else:
    h(lala[:n])
    


    
