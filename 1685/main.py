# python 2.7.3
import sys
import math

def f(origin, left, right, sentence, pos):
    if left > right:
        return
    mid = (left + right) / 2
    origin[mid] = sentence[pos[0]]   
    pos[0] += 1
    f(origin, left, mid - 1, sentence, pos)
    f(origin, mid + 1, right, sentence, pos)    

sentence = raw_input()
origin = [None for i in sentence]

pos = [0]
f(origin, 0, len(origin) - 1,sentence, pos)
print ''.join(origin)



    


    

