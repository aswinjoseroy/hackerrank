#!/usr/bin/python

t = int(input())

def primes(n):
	#Returns  a list of primes < n
	sieve = [True] * n
	for i in xrange(3,int(n**0.5)+1,2):
		if sieve[i]:
			sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
	return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def caluclate(n):
	p = primes(n+1)
#	print p
	i = 0
	lcm = 1
	for i in range(len(p)):
		m = 1
		while (p[i] ** m) <= n:
			m += 1
		lcm = lcm *  (p[i] ** (m-1))
	return lcm

for i in range(t):
	n = int(input())
	print caluclate(n)
	


