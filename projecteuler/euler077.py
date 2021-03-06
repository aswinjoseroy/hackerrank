#!/usr/bin/python
from bisect import bisect
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
# generate primes
#primes = genPrimes(1000)
# use prepopulated primes
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

#used code sample from coin changing problem tutorial
#https://www.youtube.com/watch?v=EScqJEEKC10
def change(n, coins_available, coins_so_far):
	if sum(coins_so_far) == n:
		yield coins_so_far
	elif sum(coins_so_far) > n:
		pass
	elif coins_available == []:
		pass
	else:
		for c in change(n, coins_available[:], coins_so_far+[coins_available[0]]):
			yield c
		for c in change(n, coins_available[1:], coins_so_far):
			yield c
# n is value

def change2(n, primes_sliced):
	ways = [0]*(n+1)
	ways[0] = 1
	i = 0
	while i < m:
		j = primes_sliced[i]
		while j <= n:
			ways[j] += ways[j-primes_sliced[i]]
			j += 1
		i += 1
	return ways[-1]
		

		
for i in range(t):
	n = int(input())
	# slice unused primes thanks to 
	#http://stackoverflow.com/questions/29957895/select-elements-in-array-less-than-given-integer-in-python/29957970#29957970
	primes_sliced = primes[:bisect(primes, n)]
	m = len(primes_sliced)
    # optimized version based on http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/
	print change2(n,primes_sliced)	
	#print len([s for s in change(n,primes_sliced, [])])
	