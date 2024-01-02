#!/usr/bin/env python3
""" A script that exports an employee's todo list to JSON """

import sys
import requests as req
import json

# Retrieve user ID from command-line arguments
user_id = sys.argv[1]

# URLs for user and todo data
user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

user_data = req.get(user_url).json()
username = user_data.get("username")

user_todos = req.get(todo_url).json()

# Filter completed todos
completed_todos = []
for todo in user_todos:
    if todo['completed']:
        completed_todos.append({
            'task': todo['title'],
            'completed': todo['completed'],
            'username': username
        })

# Create JSON data
json_data = {user_id: completed_todos}

# Write data to JSON file
json_filename = f"{user_id}.json"
with open(json_filename, 'w') as json_file:
    json.dump(json_data, json_file)

print(f"JSON data exported to {json_filename}")
