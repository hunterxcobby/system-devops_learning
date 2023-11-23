#!/bin/bash

cd ../notes/

for i in {1..15}
do 
    git add .
    git commit -m "add file $i"
done