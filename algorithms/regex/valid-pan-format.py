#!/usr/bin/python

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
t = int(input())

for i in range(t):
	n = raw_input().strip()
	if re.search("^[A-Z][A-Z][A-Z][A-Z][A-Z]\d\d\d\d[A-Z]",n):
		print "YES"
	else:
		print "NO"