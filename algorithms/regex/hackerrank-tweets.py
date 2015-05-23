#!/usr/bin/python

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
t = int(input())
counter = 0
string = "hackerrank"
for i in range(t):
	n = raw_input().lower()
	#print re.search(string,n)
	if re.search(string,n) != None:
		counter += 1
print counter