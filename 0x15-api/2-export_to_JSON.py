#!/usr/bin/python3

import json
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide a user ID.")
        sys.exit(1)

    uid = sys.argv[1]
    url_user = f"https://jsonplaceholder.typicode.com/users/{uid}"
    url_todo = f"https://jsonplaceholder.typicode.com/todos?userId={uid}"

    try:
        response_user = requests.get(url_user)
        response_todo = requests.get(url_todo)

        response_user.raise_for_status()
        response_todo.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err}")
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")
        sys.exit(1)

    user_data = response_user.json()
    todo_data = response_todo.json()

    if not user_data:
        print(f"User with ID {uid} not found.")
        sys.exit(1)

    username = user_data.get('username')
    tasks = [{"task": task['title'], "completed": task['completed'], "username": username} for task in todo_data]

    data = {uid: tasks}

    with open(f"{uid}.json", 'w') as json_file:
        json.dump(data, json_file)
