#!/bin/bash

# we are assigning variables
var=27
category=minerals
items=torchlight
box=torchlight

# = Test Operator:

if [ "$box" = "$items" ]
then
  echo "true"
fi
