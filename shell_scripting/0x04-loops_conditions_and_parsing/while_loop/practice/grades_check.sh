#!/bin/bash 

english=90
maths=30

while [ $english -gt $maths ]
do
    echo "You Passed English!!"
    if [ $maths -lt $english ]
    then
        echo "but you failed Maths"
        break  # Exit the loop if some_condition is true
    fi
done

