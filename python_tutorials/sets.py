#!/usr/bin/python

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
n = set(raw_input().strip().split(' '))
m = int(input())
m = set(raw_input().strip().split(' '))
mn = m.symmetric_difference(n)
mn = list(mn)
mn = map(int,mn)
mn = sorted(mn)
for i in range(len(mn)):
	print mn[i]
#mn = m.difference(n)
#for i in range(len(mn)):

