# python 2.7.3
import sys
import math

def main():
    data = raw_input()

    pos = -1
    for i in range(len(data) - 1, -1, -1):
        if data[i] != '0':
            pos = i
            break
    # all digits are 0
    if pos == -1:
        print -1
        return
    
    for i in range(pos - 1, -1, -1):
        if data[i] != '9':
            result = map(int, list(data))
            result[i] += 1
            temp = sum(result[(i + 1):]) - 1
            result = result[:(i + 1)] + [0] * (len(result) - 1 - i)
            pos = len(result) - 1
            while temp > 0:
                if temp >= 9:
                    result[pos] = 9
                    temp -= 9
                else:
                    result[pos] = temp
                    temp = 0
                pos -= 1
            print ''.join(map(str, result))
            break
    else:
        print -1        

main()
    

    


    

