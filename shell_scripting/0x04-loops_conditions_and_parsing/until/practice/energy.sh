#!/bin/bash

energy=1000

until [ $energy -eq 0 ]
do
    echo "I am not giving up"

    if [ $energy -eq 500 ]
    then
        echo "I need a bit of rest"
        sleep 2
    fi

    ((energy--))
done
