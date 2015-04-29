#!/usr/bin/python


# Complete the function below.

def  maxXor( l,  r):
	diff = r-l
	dict = {}
	for i in range(diff+1):
		j = 0
		while j <= i:
			xor = (l + i) ^ (l + j)
			dict['('+str(l + j)+')('+str(l + i)+")"] = xor
			j += 1
	return dict[max(dict, key=dict.get)]


_l = int(raw_input());


_r = int(raw_input());

res = maxXor(_l, _r);
print(res)

