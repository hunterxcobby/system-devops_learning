#!/usr/bin/python3
import requests
import sys

def get_employer_details(employee_id):
    url_path = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url_path)

    if response.status_code == 200:
        employee_data = response.json()
        print(employee_data)
        employee_name = employee_data[0]["id"]
        total_tasks = len(employee_data)
        completed_tasks = sum(1 for task in employee_data if task["completed"])

        print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
        for task in employee_data:
            if task["completed"]:
                print(f"\t{task['title']}")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

def main():
    if len(sys.argv) != 2:
        print("Please provide an employee ID as an argument.")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employer_details(employee_id)

if __name__ == "__main__":
    main()
