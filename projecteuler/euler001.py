#!/usr/bin/python

# https://www.hackerrank.com/contests/projecteuler/challenges/euler001

#number of testcases
t = int(input())

#bruteforce
#thanks to http://www.mathblog.dk/project-euler-problem-1/
def calculate(n):
	i = 0
	result = 0
	while i < n:
		if i % 3 == 0 or i % 5 == 0:
			result += i
		i += 1
	return result


# arithmetic

def calculate2(n):
	result = sumDivisible(3,n - 1)+sumDivisible(5,n - 1)-sumDivisible(15,n - 1)
	return result
def sumDivisible(n, p):
	return n*(p/n)*((p/n)+1)/2
		
for i in range(t):
	n = int(input())
	# brute force O(n)
	#print calculate(n)
	# arithmetic O(1)
	print calculate2(n)
	