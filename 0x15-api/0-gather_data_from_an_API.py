#!/usr/bin/python3 
"""
Employee Task Summary Script

This script retrieves information about a user and their completed tasks from the JSONPlaceholder API.
It takes a user ID as a command-line argument, fetches the user's details, and prints a summary of
completed tasks along with their titles.

Usage:
    python3 0-gather_data_from_an_API.py <user_id>
"""

import requests as req
import sys

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
