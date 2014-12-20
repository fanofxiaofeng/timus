# python 2.7.3
import sys
import math

class R:
	def __init__(self, num, den = 1):
		self.num = num
		self.den = den
	def __repr__(self):
		return "%d %d" % (self.num, self.den)
	def __gt__(self, rhs):
		return self.num * rhs.den >= self.den * rhs.num
	def __sub__(self, rhs):
		return R(self.num * rhs.den - self.den * rhs.num, self.den * rhs.den)
	def __add__(self, rhs):
		return R(self.num * rhs.den + self.den * rhs.num, self.den * rhs.den)
	def __div__(self, rhs):
		return R(self.num * rhs.den, self.den * rhs.num)
	def __mul__(self, rhs):
		return R(self.num * rhs.num, self.den * rhs.den)
	def __int__(self):
		return self.num / self.den

def toR(num, den = 1):
	return R(num, den)

n = input()
data = map(int, sys.stdin.readline().split())
total = sum(data)

data = map(toR, data)

average = R(total, (n + 1))
# print "average:", average
record = [R(0) for i in data]

above = R(0)
for i in range(len(data)):
	if data[i] > average:		
		record[i] = data[i] - average
		above = above + record[i]
rouble = R(100) / above
ans = map(lambda x: x * rouble, record)
print ' '.join(map(str, map(int, ans)))
