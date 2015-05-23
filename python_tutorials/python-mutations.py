#!/usr/bin/python

# Enter your code here. Read input from STDIN. Print output to STDOUT
string = str(raw_input())

l = str(raw_input()).split(' ')
n = int(l[0])
m = n + 1
string = string[:n] + l[1] + string[m:]
print string
