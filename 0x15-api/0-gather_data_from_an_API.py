#!/usr/bin/python3
""" A script that returns an employee's todo list """

import sys
import requests as req

user_id = sys.argv[1]

url = "https://jsonplaceholder.typicode.com/users/{}"
url2 = "https://jsonplaceholder.typicode.com/todos?userId={}"

user_url = url.format(user_id)
todo_url = url2.format(user_id)

user_data = req.get(user_url).json()
username = user_data.get("name")

user_todos = req.get(todo_url).json()
total = len(user_todos)

completed_todos = []
for todo in user_todos:
    if todo['completed']:
        completed_todos.append(todo)
completed = len(completed_todos)

print("Employee {} is done with tasks({}/{})"
        .format(username, completed, total))
for todo in completed_todos:
    print("     {}".format(todo['title']))
