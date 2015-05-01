#!/usr/bin/python

# https://www.hackerrank.com/contests/projecteuler/challenges/euler001

#number of testcases
t = int(input())

def calculate(n):
	i = 0
	result = 0
	while i < n:
		if i % 3 == 0 or i % 5 == 0:
			result += i
		i += 1
	return result
		
for i in range(t):
	n = int(input())
	print calculate(n)
	