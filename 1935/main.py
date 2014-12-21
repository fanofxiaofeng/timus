# python 2.7.3
import sys
import math

_ = input()
data = map(int, sys.stdin.readline().split())
print sum(data) + max(data)
