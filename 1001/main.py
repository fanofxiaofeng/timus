# python 3.4.0
import sys
import math

data = []
for line in sys.stdin:
    for num in line.split():
        data.append(num)

# print(data)
data.reverse()
for i in data:
    print("%.4f" % math.sqrt(float(i)))
    

