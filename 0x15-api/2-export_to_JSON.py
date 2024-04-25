#!/usr/bin/python3
'''
A script to export data in the JSON format.
'''

import json
import requests
from sys import argv

if __name__ == '__main__':
    uid = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(uid)
    user = requests.get(url, verify=False).json()
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(uid)
    todos = requests.get(url, verify=False).json()
    name = user.get('username')
    todo = [{"task": todo.get("title"),
          "username": name,
          "completed": todo.get("completed")} for todo in todos]
    content = {}
    content[uid] = todo
    with open("{}.json".format(uid), 'w') as filejs:
        json.dump(content, filejs)
