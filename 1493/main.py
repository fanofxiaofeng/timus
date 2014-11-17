# python 2.7.3
import sys
import math


def cal(a):
    a = str(a)
    s = 0
    for i in a:
        s += int(i)
    return s

num = sys.stdin.readline()
num = int(num)

found = False

temp = num - 1
if cal(temp / 1000) == cal(temp % 1000):
    found = True

temp = num + 1
if cal(temp / 1000) == cal(temp % 1000):
    found = True

if found:
    print "Yes"
else:
    print "No"
    


    

