#!/bin/bash

energy=10

until [ $energy -eq 0 ]
do
    echo "I am not giving up"
    ((energy--))
done
