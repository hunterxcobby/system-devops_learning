#!/bin/bash

energy=10

until [ $energy -eq 0 ]
do
    echo "I am not giving up"

    if [ $energy -eq 5 ]
    then
        echo "I need a bit of rest"
    fi

    ((energy--))
done
