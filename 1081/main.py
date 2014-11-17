# python 2.7.3
import sys
import math

def init():
    ans = [1, 2]
    for i in range(50):
        ans.append(ans[-1] + ans[-2])
    return ans

ans = init()

[n, k] = map(int, sys.stdin.readline().split())

if k > ans[n]:
    print -1
else:
    # k <= ans[n]
    result = ''
    while len(result) < n:
        if k <= ans[n - 1 - len(result)]:
            result += '0'
        else:
            k -= ans[n - 1 - len(result)]            
            result += '1'
            if len(result) < n:
                result += '0'
    print result

