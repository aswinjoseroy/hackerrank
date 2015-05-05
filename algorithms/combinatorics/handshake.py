#!/usr/bin/python

t = int(input())

for i in range(t):
	n = int(input())
	
	#handshake number
	h = n * (n - 1)
	h = h/2
	print h
	i += 1