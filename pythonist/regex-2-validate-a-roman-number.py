#!/usr/bin/python

import re
a = str(raw_input())

regex = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'

if re.search(regex,a) == None:
	print False
else:
	print True