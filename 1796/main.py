# python 2.7.3
import sys
import math

def ceil(a, b):
    return a / b + (a % b != 0)

notes = [10, 50, 100, 500, 1000, 5000] 
   
data = sys.stdin.readline().split()
n = input()

for i in range(len(data)):
    data[i] = int(data[i])

upper = 0
for i in range(len(notes)):
    upper += notes[i] * data[i]

lower = upper
for i in range(len(notes)):
    if data[i] != 0:
        lower = upper - notes[i]
        break
lower += 1

s = ''
result = range(ceil(lower, n), upper / n + 1)
print len(result)
for i in result:
    if not s:
        s += str(i)
    else:
        s += ' ' + str(i)
print s





    

