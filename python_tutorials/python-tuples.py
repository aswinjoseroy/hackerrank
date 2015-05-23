#!/usr/bin/python

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
t = tuple(int(x.strip()) for x in raw_input().split(' '))
print hash(t)