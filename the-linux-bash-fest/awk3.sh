#!/bin/bash

awk '{
    if(($2 + $3 + $4)/3 <= 50)
        print $1, $2, $3, $4,":","FAIL";
    else if(($2 + $3 + $4)/3 >= 60 && ($2 + $3 + $4)/3 <= 80)
        print $1, $2, $3, $4,":","B";
    else
        print $1, $2, $3, $4,":","A";
}'


search engine start with
that doesnt exist 

read line1
read line2
arr=($line2)

j = 0
for i in ${arr[@]}; 
do 
 tmp = $j ^ $i; 
done
echo $tmp