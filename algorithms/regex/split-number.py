#!/usr/bin/python

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
t = int(input())
for i in range(t):
	n = raw_input()
	a = re.compile("(\w{1,3}[\s|-])(\w{1,3}[\s|-])(\w{4,10}$)")
	res = re.search(a,n)
	print "CountryCode=" + res.group(1).strip('-').strip(' ') + "," + "LocalAreaCode=" + res.group(2).strip('-').strip(' ') + "," + "Number=" + res.group(3)

