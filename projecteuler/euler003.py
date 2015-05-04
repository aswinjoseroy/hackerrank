#!/usr/bin/python
#Project Euler #3: Largest prime factor

from math import sqrt
from bisect import bisect

t = int(input())

def primes(n):
	#Returns  a list of primes < n
	sieve = [True] * n
	for i in xrange(3,int(n**0.5)+1,2):
		if sieve[i]:
			sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
	return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def caluclate(n):
	i = 0
	while i < range(len(p)):
		if n % primes_sliced[i] == 0:
			return primes_sliced[i]
		else:
			i += 1
def is_prime(n):
	"""Return True if n is a prime number (1 is not considered prime)."""
	if n < 3:
		return (n == 2)
	elif n % 2 == 0:
		return False
	elif any(((n % x) == 0) for x in xrange(3, int(sqrt(n))+1, 2)):
		return False
	return True
	
def largest_prime_factor(n):
	i = 2
	while i * i <= n:
		if n % i:
			i += 1
		else:
			n //= i
	return n
			
p = primes(int(sqrt(10000000000)+1))
	
for i in range(t):
	n = int(input())
	
	if is_prime(n):
		print n
	else:
		#p = primes(1n+1)
		primes_sliced = p[:bisect(p, n)]
		primes_sliced.reverse()
		p.reverse()
		print largest_prime_factor(n)
	