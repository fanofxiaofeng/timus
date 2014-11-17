# python 2.7.3
# Give post-order traversal, output the 'mirror' post-order traversal
# Failed with Python, AC with C++. The file is in the corresponding folder.
import sys
import math

class node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def getValue(self):
        return self.value

def f(data, start, end):
    # start and end are the starting position and end position respectively
    # return a node
    
    root = node(data[end])
    # print 'value at root: %d', root.getValue()
    
    if end == start:
        return root
    
    hasLeft = (data[start] < root.getValue())
    hasRight = (data[end - 1] > root.getValue())

    if not hasLeft:
        root.right = f(data, start, end - 1)
        return root
    if not hasRight:
        root.left = f(data, start, end - 1)
        return root
    # both left child and right right exist
    low = start
    high = end - 1
    while True:
        mid = (low + high) / 2
        if data[mid] < root.getValue():
            low = mid + 1
        elif data[mid - 1] > root.getValue():
            high = mid - 1
        else:
            break
    root.left = f(data, start, mid - 1)
    root.right = f(data, mid, end - 1)
    return root
    
def mirrorPre(root, result):
    if root.right:
        mirrorPre(root.right, result)
    if root.left:
        mirrorPre(root.left, result)
    result.append(root.getValue())

n = input()
data = []
while len(data) != n:
    temp = sys.stdin.readline().split()
    data.extend(temp)
for i in range(len(data)):
    data[i] = int(data[i])

root = f(data, 0, len(data) - 1)
result = []
mirrorPre(root, result)
s = ''
for i in result:
    if s:
        s += ' ' + str(i)
    else:
        s += str(i)
print s



    
    



    

