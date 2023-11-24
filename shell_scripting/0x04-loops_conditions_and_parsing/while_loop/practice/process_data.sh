#!/bin/bash

data=1

while [ "$data" -le 5 ]
do
    if [ "$data" -eq 3 ]
    then
        echo "We do not need to process data $data"
        ((data++))
        continue  # Skip the rest of the loop body and move to the next iteration
    fi

    echo "Processing data $data"
    ((data++))
done
