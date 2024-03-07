#!/usr/bin/python3
import requests
import sys



def check_arg(args):
    if len(args) != 2:
        print("Please made sure to id and nothing else")
    else:
        employee_id = sys.argv[1]
        return employee_id
    
id = check_arg(args = sys.argv)

def getEmployersDetails(id):
    print(id)

getEmployersDetails(id)