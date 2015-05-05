#!/usr/bin/python

a = int(input())
b = raw_input()

l = map(int, b.split())
l = sorted(list(set(l)))
print l[len(l)-2]
