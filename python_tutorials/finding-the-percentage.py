#!/usr/bin/python

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
b = {}
for i in range(n):
	a = raw_input().split(' ')
	b[a[0]] = float(a[1])+float(a[2])+float(a[3])
print "%.2f" % float(b[raw_input()]/3)