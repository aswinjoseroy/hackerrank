#!/usr/bin/python

#X = int(input()) 
#Y = int(input()) 
#Z = int(input()) 
#N = int(input()) 
#x = 1
#y = 1
#z = 1
#n = 2

x = int(input()) 
y = int(input()) 
z = int(input()) 
n = int(input())

listX =[x for x in range(x+1)] 
listY =[y for y in range(y+1)] 
listZ =[z for z in range(z+1)] 
list =[]

for i in listX: 
	for j in listY: 
		for k in listZ:
			if  i+j+k != n: 
				list.append([i,j,k]) 
print(list)