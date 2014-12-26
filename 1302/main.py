# python 2.7.3
import sys
import math

# N = 32000 is big enough
N = 32000
num = range(N)
square = map(lambda x: x * x, num)
# print square

def getInfo(k):
	pos = 1
	while True:
		if square[pos] >= k:
			delta = k - square[pos - 1]
			if delta % 2 == 0:
				return [2 * (pos - 1), delta]
			else:
				return [2 * pos - 1, delta]			
		pos += 1

def calc(mInfo, nInfo):
	mRow, mCol = mInfo
	nRow, nCol = nInfo
	mDelta = mRow - mCol # non-negtive
	nDelta = nRow - nCol # non-negtive
	if mDelta > nDelta: # make sure that m is nearer to the right bound
		return calc(nInfo, mInfo)
	mSum = mRow + mCol
	nSum = nRow + nCol
	diffOfDelta = abs(mDelta - nDelta) / 2
	diffOfSum = abs(mSum - nSum) / 2
	if diffOfSum >= diffOfDelta:
		return diffOfSum + diffOfDelta
	else:
		if mRow % 2 == 0:
			if diffOfSum % 2 == 0:
				return 2 * diffOfDelta
			else:
				return 2 * diffOfDelta - 1
		else:
			if diffOfSum % 2 == 0:
				return 2 * diffOfDelta + 1
			else:
				return 2 * diffOfDelta
	pass

[m, n] = map(int, sys.stdin.readline().split())

mInfo = getInfo(m)
# print mInfo

nInfo = getInfo(n)
# print nInfo
print calc(mInfo, nInfo)

