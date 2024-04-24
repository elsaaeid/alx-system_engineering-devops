#!/usr/bin/python3

import json
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

# Prepare the data for the JSON file
data = {user_id: [{"task": task['title'], "completed": task['completed'], "username": username} for task in tasks]}

# Write the data to a JSON file
with open(f'{user_id}.json', 'w') as jsonfile:
    json.dump(data, jsonfile)

