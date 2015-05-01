#!/usr/bin/python

t = int(input())

# http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188

def primes(n):
	""" Returns  a list of primes < n """
	sieve = [True] * n
	for i in xrange(3,int(n**0.5)+1,2):
		if sieve[i]:
			sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
	return [2] + [i for i in xrange(3,n,2) if sieve[i]]

p = primes(100000)
for i in range(t):
	n = int(input())
	print p[n-1]