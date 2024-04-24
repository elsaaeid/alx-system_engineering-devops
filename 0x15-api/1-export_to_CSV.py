#!/usr/bin/python3

import csv
import requests
import sys

# Get the user ID from the command line arguments
user_id = sys.argv[1]

# Send a GET request to the JSONPlaceholder API
response = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}/todos')

# Parse the JSON response
tasks = response.json()

# Get the username
username = tasks[0]['username']

# Prepare the data for the CSV file
data = [[task['userId'], username, task['completed'], task['title']] for task in tasks]

# Write the data to a CSV file
with open(f'{user_id}.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    writer.writerows(data)
