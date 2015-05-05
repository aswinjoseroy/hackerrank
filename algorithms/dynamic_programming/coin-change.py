#!/usr/bin/python

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
		

		
#amount and type
at = [int(i) for i in raw_input().strip().split()]
#at = [10, 4]
#list of coins
list = [int(i) for i in raw_input().strip().split()]
#list = [2, 5, 3, 6]
m = len(list)

print change2(at[0],list)	

