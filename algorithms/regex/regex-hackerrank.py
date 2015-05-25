#!/usr/bin/python

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
t = int(input())
string = "hackerrank"
for i in range(t):
	out = ""
	n = raw_input().strip()
	if re.search("^"+string, n):
		out = "1"
	elif re.search(string+"$",n):
		out = "2"
	else:
		out = "-1"
	if re.search("^(hackerrank)$",n):
		out = "0"
		
	print out