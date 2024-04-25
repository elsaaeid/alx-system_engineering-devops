#!/usr/bin/python3
import json
import requests

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(url, verify=False).json()
    undoc = {}
    udoc = {}
    for user in users:
        uid = user.get("id")
        udoc[uid] = []
        undoc[uid] = user.get("username")
    url = "https://jsonplaceholder.typicode.com/todos"
    todos = requests.get(url, verify=False).json()
    [udoc.get(todo.get("userId")).append({"task": todo.get("title"),
                                       "completed": todo.get("completed"),
                                       username": undoc.get(
                                               todo.get("userId"))})
     for todo in todos]
    with open("todo_all_employees.json", 'w') as jsf:
        json.dump(udoc, jsf)
