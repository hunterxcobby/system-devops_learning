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
    
    url_path = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    print(url_path.status_code)
    print(id)

getEmployersDetails(id)