#!/usr/bin/python3

"""
This script retrieves information about users and their completed
tasks from the JSONPlaceholder API and exports the data in
JSON formats.
"""

import json
import requests
import sys


def get_user_data(user_id):
    """
    Fetches user data from the JSONPlaceholder API.
    """
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    return requests.get(user_url).json()


def get_user_todos(user_id):
    """
    Fetches user's to-do list from the JSONPlaceholder API.
    """
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    return requests.get(todo_url).json()


def export_to_json():
    """
    Exports all users' completed tasks to a JSON file.
    """
    all_employees_data = {}

    for user_id in range(1, 11):
        user_data = get_user_data(user_id)
        username = user_data.get("username")

        user_todos = get_user_todos(user_id)
        completed_todos = [
            {
                "username": username,
                "task": todo["title"],
                "completed": todo["completed"],
            }
            for todo in user_todos
            if todo["completed"]
        ]

        all_employees_data[str(user_id)] = completed_todos

    filename = "todo_all_employees.json"
    with open(filename, "w", encoding="utf-8") as jsonfile:
        json.dump(all_employees_data, jsonfile)


def main():
    """
    Main function to execute the script.
    """
    export_to_json()


if __name__ == "__main__":
    main()
