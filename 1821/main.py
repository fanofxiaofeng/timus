# python 2.7.3
import sys
import math

def convert(time):
    m = int(time[:time.index(':')])
    s = int(time[time.index(':') + 1:time.index('.')])
    d = int(time[-1])
    t = 10 * (m * 60 + s) + d
    return t

n = input()

finish_name = {}
finish_time = {}
for i in range(n):
    name, time_str = sys.stdin.readline().split()
    time = convert(time_str)
    finish = time + 300 * i
    finish_name[finish] = name
    finish_time[finish] = time
li = finish_name.keys()
li.sort()

result = []
opt = 1000000
for i in li:
    if finish_time[i] < opt:
        opt = finish_time[i]
        result.append(finish_name[i])
result.sort()
print len(result)
for i in result:
    print i

    
    

