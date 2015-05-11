#!/usr/bin/python
from operator import itemgetter, attrgetter, methodcaller

a = "2 3"
b = raw_input().split(' ')
#b = a.split(' ')
m = int(b[0])
n = int(b[1])
nn = []
#print m
for i in range(m):
	n=raw_input().split(' ')
	nn.append(n)
k = int(input())
print k
l =[]
for i in range(len(nn)):
	l.append(int(nn[i][k]))
print sorted(l)
	