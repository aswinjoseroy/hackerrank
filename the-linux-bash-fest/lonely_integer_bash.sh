#!/bin/bash

awk '{
if (NR == 1)
    n = $0
if (NR == 2)
    split($0,a," ")
j = 0
for (i = 0; i <= n; i++)
    j = xor(j,a[i])
if (NR == 2)
    print j
}'

