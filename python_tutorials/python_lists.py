#!/usr/bin/python

# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
l = []
for i in range(t):
	n = str(raw_input()).strip().split(' ')
	if n[0] == "print":
		print l
	elif n[0] == "insert":
		l.insert(int(n[1]),int(n[2]))
	elif n[0] == "remove":
		l.remove(int(n[1]))
	elif n[0] == "sort":
		l.sort()
	elif n[0] == "reverse":
		l.reverse()
	elif n[0] == "pop":
		l.pop()
	elif n[0] == "append":
		l.append(int(n[1]))