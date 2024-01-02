#!/usr/bin/env python3
""" A script that returns an employee's todo list """

import sys
import requests as req
import csv

# Retrieve user ID from command-line arguments
user_id = sys.argv[1]

# URLs for user and todo data
user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)

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

# Define CSV file name
csv_filename = f"{user_id}.csv"

# Write data to CSV file
with open(csv_filename, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    for todo in user_todos:
        # Write each todo as a row in the CSV file
        csv_writer.writerow([user_id,username,str(todo['completed']),todo['title']])

print(f"CSV data exported to {csv_filename}")
