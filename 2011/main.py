# python 2.7.3
import sys
import math

def choose(n, k, fac):
    return fac[n] / fac[k] / fac[n - k]

n = input()
data = sys.stdin.readline().split()

m = {'1': 0, '2': 0, '3': 0}
for i in range(n):
    m[data[i]] += 1

big = 120
fac = [1] * big
for i in range(1, big):
    fac[i] = fac[i - 1] * i

result = choose(n, m['1'], fac) * choose(m['2'] + m['3'], m['2'], fac)

if result >= 6:
    print 'Yes'
else:
    print 'No'

    
