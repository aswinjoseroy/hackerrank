#!/usr/bin/python

def insertionSort(ar, m):
	last = ar[m-1]
	for i in reversed(range(m)):
		# if 3 < 8
		if ar[i-1] > last and i > 0:
			ar[i] = ar[i-1]
		 	i += 1
		elif ar[i-1] < last:
			ar[i] = last
			print ' '.join(str(e) for e in ar)
			break
		else:
			ar[0] = last
		
		print ' '.join(str(e) for e in ar)
m = input()
#m = 5
ar = [int(i) for i in raw_input().strip().split()]
#ar = [2,3,4,5,6,7,8,9,10,1]
#ar = [2,4,6,8,3]
insertionSort(ar, m)

