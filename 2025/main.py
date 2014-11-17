# python 2.7.3
import sys
import math

def f(n, k):
    s = n * n
    a = n / k
    b = n % k
    temp = s - b * (a + 1) ** 2 - (k - b) * a ** 2
    return temp / 2

T = input()

for i in range(T):
    [n, k] = map(int, sys.stdin.readline().split())
    print f(n, k)


    
