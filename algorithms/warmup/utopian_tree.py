#!/usr/bin/python

# https://www.hackerrank.com/challenges/utopian-tree
#read numbers of tests
for i in range(input()):
	#read number of years for test
	n = int(input())
	#tree heigh
	h = 1
	m = 1
	while m <= n:
		if m % 2 != 0:
			h = h * 2
		else:
			h = h + 1
		m = m +1
	print h


