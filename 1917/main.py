# python 2.7.3
import sys
import math

n, p = map(int, sys.stdin.readline().split())
data = map(int, sys.stdin.readline().split())

m = {}
for i in data:
    m[i] = m.get(i, 0) + 1

data = m.keys()
data.sort()

n_cnt = 0
level_cnt = 0
for i in range(len(data)):
    key = data[i]
    temp = key * m[key]
    if temp > p:        
        break    
    n_cnt += m[key]
    level_cnt += 1

if level_cnt == 0:
    print 0, 0
else:
    temp_level = 0    
    cast_cnt = 1
    coin_cnt = 0
    while temp_level  < level_cnt:
        coin_cnt += m[data[temp_level]]
        total_cost = coin_cnt * data[temp_level]
        if total_cost > p:
            cast_cnt += 1
            coin_cnt = m[data[temp_level]]           
        temp_level += 1
    print n_cnt, cast_cnt
        

    
    
    
