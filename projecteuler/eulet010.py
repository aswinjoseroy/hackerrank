#!/usr/bin/python

t = int(input())
from bisect import bisect

def primes(n):
	""" Returns  a list of primes < n """
	sieve = [True] * n
	for i in xrange(3,int(n**0.5)+1,2):
		if sieve[i]:
			sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
	return [2] + [i for i in xrange(3,n,2) if sieve[i]]

p = primes(1000000)

for i in range(t):
	n = int(input())
	primes_sliced = p[:bisect(p, n)]
	print(sum(primes_sliced))