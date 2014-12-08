# python 2.7.3
import sys
import math

class Hero:
	def __init__(self, id, need):
		self.id = id
		self.need = need

	def getId(self):
		return self.id

	def getNeed(self):
		return self.need

	@staticmethod
	def cmp(h1, h2):
		if h1.getNeed() != h2.getNeed():
			if h1.getNeed() < h2.getNeed():
				return -1
			else:
				return 1
		else:
			if h1.getId() < h2.getId():
				return -1
			elif h1.getId() > h2.getId():
				return 1
			else:
				return 0
	
n = input()
heroes = [None for i in range(n)]

for i in range(n):
	heroes[i] = Hero(i + 1, input())

heroes.sort(Hero.cmp)

result = []
ids = map(lambda x: x.getId(), heroes)
for i in range(len(heroes)):
	cnt = i + 1
	hero = heroes[i]
	if hero.getNeed() > cnt:
		continue
	if i + 1 == len(heroes):
		temp = [len(heroes)]
		temp.extend(range(1, n + 1))
		result.append(temp)
		continue
	next = i + 1
	if heroes[next].getNeed() <= cnt + 1:
		continue
	else:
		# heroes[next].getNeed() >= cnt + 2
		temp = [cnt]		
		temp.extend(ids[:cnt])
		result.append(temp)
print len(result)
for row in result:
	print ' '.join(map(lambda x: str(x), row))
