#!/usr/bin/python
import re
t = int(input())

#starts with regexp
regex = '^[7,8,9][0-9]+$'
def check(n):
	if len(n) == 10 and re.search(regex,n) != None:
		return "YES"
	else:
		return "NO"

for i in range(t):
	n = str(raw_input())
	print check(n)
