# python 2.7.3
import sys
import math

class Diamond:
	def __init__(self, info):
		self.info = list(info)
			
	@staticmethod
	def cmp(a, b):
		if a[0] != b[0]:
			return False		
		c = [None]
		c.extend(b[-1])
		c.extend(b[-1])
		for delta in range(3):
                        valid = True
                        for i in range(1, 4):
                                if a[i] != c[i + delta]:
                                        valid = False
                                        break
                        if valid:
                                return True                                
		return False


	def __eq__(self, rhs):
		s = self.getInfo()
		r = rhs.getInfo()
		
		# 0 as bottom
		if Diamond.cmp(s, [r[0], [r[1], r[2], r[3]]]):
			return True
		# 1 as bottom
		if Diamond.cmp(s, [r[1], [r[3], r[2], r[0]]]):
			return True
		# 2 as bottom
		if Diamond.cmp(s, [r[2], [r[0], r[1], r[3]]]):
			return True
		# 3 as bottom
		if Diamond.cmp(s, [r[3], [r[2], r[1], r[0]]]):
			return True
		return False
	
	def getInfo(self):
		return (self.info)[:]

d1 = Diamond(raw_input())
d2 = Diamond(raw_input())

if d1 == d2:
	print "equal"
else:
	print "different"
