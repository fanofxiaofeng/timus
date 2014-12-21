# python 2.7.3
import sys
import math

[n, k] = map(int, sys.stdin.readline().split())

print n * (n - 1) / 2 - k
