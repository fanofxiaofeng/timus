# python 2.7.3
import sys
import math

class Sieve:
	def __init__(self, bound):
		assert(bound >= 2)
		self.bound = bound
		self.record = [0 for i in range(bound + 1)]
		for i in range(2, len(self.record)):
			if self.record[i] == 0:
				for j in range(i + i, len(self.record), i):
					if self.record[j] == 0:
						self.record[j] = i
		# print self.record
		
	def getPrimeFactors(self, n):
		assert(n > 0 and n <= self.bound)
		m = {}
		if n == 1:
			return m
		while(self.record[n] != 0):
			f = self.record[n]
			m[f] = m.get(f, 0) + 1
			n /= f	
		m[n] = m.get(n, 0) + 1
		return m

def mapCombine(m1, m2):
	for item, value in m2.items():
		m1[item] = m1.get(item, 0) + value

s = Sieve(10010)
m = {}
for i in range(10):
	n = input()
	mapCombine(m, s.getPrimeFactors(n))
# print m

ans = 1
for item, value in m.items():
	ans *= (value + 1)
print ans % 10
