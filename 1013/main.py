# python 2.7.3
import sys
import math

def mul(left, right, m):
	result = [[0, 0], [0, 0]]
	for row in range(2):
		for col in range(2):
			temp = 0
			for i in range(2):
				temp += left[row][i] * right[i][col]
			result[row][col] = temp % m
	return result
			

def calc(matrix, p, m):
	if p == 1:
		return matrix
	temp = calc(matrix, p / 2, m)
	temp = mul(temp, temp, m)
	if p % 2 == 0:
		return temp
	else:
		return mul(temp, matrix, m)
	

n = input()
k = input()
m = input()

matrix = [[k - 1, k - 1], [1, 0]]
# print mul(matrix, matrix, 1000)
result = calc(matrix, n - 1, m)
temp = result[0][0] * (k - 1) + result[1][0] * (k - 1)
print temp % m

