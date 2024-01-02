#!/usr/bin/python3

"""
This script retrieves information about a user and their completed
tasks from the JSONPlaceholder API.
"""

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


def main():
    """Main function to execute the script."""
    user_id = sys.argv[1]
    user_data = get_user_data(user_id)
    username = user_data.get("name")

    user_todos = get_user_todos(user_id)
    total = len(user_todos)

    completed_todos = [todo for todo in user_todos if todo.get('completed')]
    completed = len(completed_todos)

    print(f"Employee {username} is done with tasks ({completed}/{total}):")
    for todo in completed_todos:
        print(f"\t{todo['title']}")


if __name__ == "__main__":
    main()
