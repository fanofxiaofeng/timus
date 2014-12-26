# python 2.7.3
import sys
import math

cnt1 = 0
cnt2 = 0
while True:
	try:
		line = raw_input()
		ans = []
		start = 0
		for i in range(len(line)):
                        if line[i] in " .,:!?-":
                                ans.append(line[start:i])
                                start = i + 1
                ans.append(line[start:])
                #print ans
		cnt1 += ans.count("tram")
		cnt2 += ans.count("trolleybus")
	except:
		break
# print cnt1, cnt2
if cnt1 > cnt2:
	print "Tram driver"
elif cnt1 < cnt2:
	print "Trolleybus driver"
else:
	print "Bus driver"
