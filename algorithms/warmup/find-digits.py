#!/usr/bin/python

# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for i in range(t):
	n = int(input())
	nstr = str(n)
	counter = 0
	for j in range(len(nstr)):    
		if int(nstr[j]) != 0 and n % int(nstr[j]) == 0:
			counter += 1
	print counter
		