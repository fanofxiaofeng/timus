# python 2.7.3
import sys
import math

def within(n, r, c):
    return (1 <= r and r <= n) and (1 <= c and c <= n)

n = input()

[r, c] = map(int, sys.stdin.readline().split())

# King
cnt = 0
for deltaR in range(-1, 1 + 1):
    for deltaC in range(-1, 1 + 1):
        if deltaR == 0 and deltaC == 0:
            continue
        if within(n, r + deltaR, c + deltaC):
            cnt += 1
print 'King: %d' % cnt

# Knight
cnt = 0
for deltaR in range(-2, 2 + 1):
    for deltaC in range(-2, 2 + 1):
        if not (deltaR ** 2 + deltaC ** 2 == 5):
            continue
        if within(n, r + deltaR, c + deltaC):
            cnt += 1
print 'Knight: %d' % cnt

# Bishop
cnt = 0
cnt += n - abs(r - c - (1 - 1))
cnt += n - abs(r + c - (n + 1))
cnt -= 1
cnt -= 1
print 'Bishop: %d' % cnt

# Rook
cnt = 0
cnt += n
cnt += n
cnt -= 1
cnt -= 1
print 'Rook: %d' % cnt

# Queen
cnt = 0
cnt += n - abs(r - c - (1 - 1)) - 1
cnt += n - abs(r + c - (n + 1)) - 1
cnt += n - 1
cnt += n - 1
print 'Queen: %d' % cnt
