# python 2.7.3
import sys
import math

def convert(s):
    if '.' in s:
        value = int(s[:s.index('.')]) * 100 + int(s[s.index('.') + 1:])
    else:
        value = int(s) * 100
    return value

data = []
while len(data) != 2:
    data.extend(sys.stdin.readline().split())
data = map(convert, data)
low, high = data


i = 1
while True:
    start = i * low / 10000 + 1
    bound = i * high / 10000
    if i * high % 10000 == 0:
        bound -= 1
    if bound >= start:
        print start
        print i
        break
    i += 1

