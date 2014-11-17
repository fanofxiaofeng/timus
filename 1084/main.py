# python 2.7.3
import sys
import math

[gl, cl] = map(float, sys.stdin.readline().split())
if cl <= gl / 2.0:
    area = math.pi * cl ** 2
elif cl >= gl / math.sqrt(2):
    area = gl ** 2
else:
    theta = math.acos((gl / 2.0) / cl)
    triangle_area = cl * math.sin(theta) * cl * math.cos(theta) / 2.0
    sector_area = cl * (math.pi / 4.0 - theta) * cl / 2.0
    area = (triangle_area + sector_area) * 8.0
print "%.3f" % area
