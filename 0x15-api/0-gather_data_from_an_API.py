#!/usr/bin/python3
"""
Employee Task Summary Script

This script retrieves information about a user and their
completed tasks from the JSONPlaceholder API. It takes a user ID
as a command-line argument, fetches the user's details, and
prints a summary of completed tasks along with their titles.

Usage:
    python3 0-gather_data_from_an_API.py <user_id>
"""

import requests
import sys


def get_user_data(user_id):
    """Fetches user data from the JSONPlaceholder API.

    Args:
        user_id (int): The ID of the user.

    Returns:
        dict: User data in JSON format.
    """
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    return requests.get(user_url).json()


def get_user_todos(user_id):
    """Fetches user's to-do list from the JSONPlaceholder API.

    Args:
        user_id (int): The ID of the user.

    Returns:
        list: User's to-do list in JSON format.
    """
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    return requests.get(todo_url).json()


def main():
    """ Main function to execute the script. """
    if len(sys.argv) > 1:
        user_id = sys.argv[1]

    if not user_id:
        print("Please provide a user ID as a command-line argument.")
        sys.exit(1)

    user_data = get_user_data(user_id)
    username = user_data.get("name")

    user_todos = get_user_todos(user_id)
    total = len(user_todos)

    completed_todos = []
    for todo in user_todos:
        if todo.get('completed'):
            completed_todos.append(todo)
    completed = len(completed_todos)

    print(f"Employee {username} is done with tasks ({completed}/{total})")
    for todo in completed_todos:
        print(f"     {todo['title']}")


if __name__ == "__main__":
    main()
