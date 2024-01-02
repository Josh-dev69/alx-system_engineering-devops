#!/usr/bin/python3
""" A script that returns an employee's todo list """

import sys
import requests as req

# Retrieve user ID from command-line arguments
user_id = sys.argv[1]

# URLs for user and todo data
url = "https://jsonplaceholder.typicode.com/users/{}"
url2 = "https://jsonplaceholder.typicode.com/todos?userId={}"

user_url = url.format(user_id)
todo_url = url2.format(user_id)

# Fetch user data
user_data = req.get(user_url).json()
username = user_data.get("name")

# Fetch user's todos
user_todos = req.get(todo_url).json()
total = len(user_todos)

# Filter completed todos
completed_todos = []
for todo in user_todos:
    if todo['completed']:
        completed_todos.append(todo)
completed = len(completed_todos)

# Print task details
print("Employee {} is done with tasks({}/{})"
        .format(username, completed, total))
for todo in completed_todos:
    print("     {}".format(todo['title']))
