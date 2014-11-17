# python 3.4.0
import sys
import math

x = sys.stdin.readline().split()
for i in range(len(x)):
    x[i] = int(x[i])
x.sort()

cnt = 0
while True:
    d = []
    for i in range(1, len(x)):        
        d.append(x[i] - x[i - 1])
    cnt += 1
    d.sort()
    if d[0] == 0:
        break
    x.append(d[0])    
    x.sort()
    # print(x)
print(cnt)

    

