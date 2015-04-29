#!/usr/bin/python

#number of testcases
t = int(input())


#generate prime numbers
def genPrimes(n):
	primes = []
	#n is number of primes to generate
	for num in range(n):
		if num > 1:
			for i in range(2,num):
				if (num % 2) == 0:
					break
			else:
				primes.append(num)
	return primes
primes = genPrimes(1000)

#return max ways
def maxWays(n):
	
	return n 

for i in range(t):
	#print i
	n = int(input())
	maxWays(n)

	
