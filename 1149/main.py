# python 2.7.3
import sys
import math

n = sys.stdin.readline().split()

n = int(n[0])

A = {}

A[1] = 'sin(1)'
for i in range(2, n + 1):
    temp = A[i - 1][:-(i - 1)]
    if i % 2 == 0:
        A[i] = temp + '-sin(' + str(i) + ')' * i
    else:
        A[i] = temp + '+sin(' + str(i) + ')' * i

temp = A[1] + '+' + str(n)
for i in range(2, n + 1):
    temp = '(' + temp + ')' + A[i] + '+' + str(n + 1 - i)

print temp
    

