# python 2.7.3
import sys
import math

data = map(int, list(sys.stdin.readline().strip()))
result = ''.join(map(str, data))
for i in range((len(data) + 1) / 2, len(data)):
    if data[i] != data[len(data) - 1 - i]:
        if data[i] < data[len(data) - 1 - i]:            
            result = data[:i] + data[len(data) - 1 - i::(-1)]            
        else:
            for j in range((len(data) + 1) / 2 - 1, -1, -1):
                if data[j] != 9:
                    temp = data[:j]   
                    if j * 2 + 1 == len(data):                        
                        result = temp + [data[j] + 1] + temp[::-1]                        
                    else:
                        temp.append(data[j] + 1)
                        result = temp + [0] * (len(data) - 2 * len(temp)) + temp[::-1]
                    break
        break
print ''.join(map(str, result))
    
    

