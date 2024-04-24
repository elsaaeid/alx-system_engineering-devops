 #!/usr/bin/python3

import requests
import sys

# Get the employee ID from the command-line arguments
employee_id = sys.argv[1]

# Send a GET request to the JSONPlaceholder API to get the employee's details
response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
employee = response.json()

# Send another GET request to get the employee's 
response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')
todos = response.json()

# Calculate the total number of tasks and the number of completed tasks
total_tasks = len(todos)
NUMBER_OF_DONE_TASKS = sum(1 for todo in todos if todo['completed'])

# Print the employee's TODO list progress
print(f'Employee {employee["name"]} is done with tasks({NUMBER_OF_DONE_TASKS}/{total_tasks}):')

# Print the titles of the completed tasks
for todo in todos:
    if todo['completed']:
        print(f'\t {todo["title"]}')
