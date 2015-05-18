#ankitarun 5 months ago
#while multiplying all the elements in a list and printing the output, how is
#for i in list: ans *= i print (int(fmod(ans,1234567)))
#and
#print (functools.reduce(op.mul, s, 1) % 1234567)
#different. As, in one case solution is being accepted while in another it just passes only one testcase.

import math

t = int(input())
ans = 1
for i in range(t*2):
	result = 1
	if i % 2 == 0:
		n = int(input())
		#print n
	else:
		m = raw_input().split(' ')
		print m
		for i in m:
			ans *= int(i) 
		print ans % 1234567


