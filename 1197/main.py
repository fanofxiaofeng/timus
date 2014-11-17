# python 2.7.3
import sys
import math

def isValid(x):
    return x >= 0 and x < 8

n = input()
n = int(n)

r_data = []
c_data = []

for r_delta in range(-2, 2 + 1):
    for c_delta in range(-2, 2 + 1):
        if r_delta ** 2 + c_delta ** 2 == 5:
            r_data.append(r_delta)
            c_data.append(c_delta)
            

for i in range(n):
    cnt = 0
    line = sys.stdin.readline()
    if line.endswith('\n'):
        line = line[:-1]
        
    r = ord(line[0])
    r -= ord('a')
    
    c = int(line[1])
    c -= 1

    for j in range(len(r_data)):
        cur_r = r + r_data[j]
        cur_c = c + c_data[j]
        if isValid(cur_r) and isValid(cur_c):
            cnt += 1
    print cnt
    
    


    

