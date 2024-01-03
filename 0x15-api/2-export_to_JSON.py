#!/usr/bin/python3

"""
This script retrieves information about a user and their completed
tasks from the JSONPlaceholder API and exports the data in both CSV and JSON formats.
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


def export_to_json(user_id):
    """
    Exports user's completed tasks to a JSON file
    """
    user_data = get_user_data(user_id)
    username = user_data.get("username")

    user_todos = get_user_todos(user_id)
    completed_todos = [
        {
            "task": todo["title"],
            "completed": todo["completed"],
            "username": username,
        }
        for todo in user_todos
    ]

    filename = f"{user_id}.json"
    with open(filename, "w", encoding="utf-8") as jsonfile:
        json.dump({user_id: completed_todos}, jsonfile)

    print(f"JSON data exported to {filename}")


def main():
    """
    Main function to execute the script.
    """
    user_id = sys.argv[1]
    export_to_json(user_id)


if __name__ == "__main__":
    main()
