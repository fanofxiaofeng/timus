# python 2.7.3
import sys
import math

s = sys.stdin.readline()
if s[-1] == '\n':
    s = s[:-1]
# print '[' + s + ']'

data = [0] * len(s)
for i in range(len(s)):
    data[i] = ord(s[i]) - 97
    if i == 0:
        if data[i] < 5:
            data[i] += 26
    else:
        while data[i] < data[i - 1]:
            data[i] += 26
# print data
for i in range(len(s) - 1, 0, -1):
    data[i] -= data[i - 1]
data[0] -= 5
# print data
for i in range(len(data)):
    data[i] = chr(data[i] + 97)
print ''.join(data)
    


    

