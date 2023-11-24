#!/bin/bash

counter=1

echo "READY !!?"
sleep 1

while [ $counter -le 5 ]
do 
    echo "count: $counter"
    ((counter++))
    sleep 0.5
done

sleep 1

echo "GO !!!!"

sleep 2