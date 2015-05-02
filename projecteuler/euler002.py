#!/usr/bin/python

#Even Fibonacci numbers
#https://www.hackerrank.com/contests/projecteuler/challenges/euler002

from math import sqrt

t = int(input())

def A(n):
	list = []
	i = 2
	while F(i) < n:
		if F(i) % 2  == 0:
			list.append(F(i))
		i += 1
		
	return sum(list)
#http://stackoverflow.com/questions/494594/how-to-write-the-fibonacci-sequence-in-python
def B(n):
	arr = [2, 8,34,144,610,2584,10946,46368,196418,832040,3524578,14930352, 63245986,267914296,1134903170,4807526976,20365011074,86267571272, 365435296162,1548008755920,6557470319842,27777890035288, 117669030460994,498454011879264,2111485077978050,8944394323791464, 37889062373143906,160500643816367088,679891637638612258, 2880067194370816120]
	list = []
	i = 0
	while arr[i] < n:
		list.append(arr[i])
		i += 1		
	return sum(list)
		
def F(n):
	return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))

for i in range(t):
	n = int(input())
	print B(n)