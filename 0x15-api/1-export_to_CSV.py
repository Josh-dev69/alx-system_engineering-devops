#!/usr/bin/python3

"""
This script retrieves information about a user and their completed
tasks from the JSONPlaceholder API and exports the data in CSV format.
"""

import csv
import requests
import sys


def get_user_data(user_id):
    """Fetches user data from the JSONPlaceholder API."""
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    return requests.get(user_url).json()


def get_user_todos(user_id):
    """Fetches user's to-do list from the JSONPlaceholder API."""
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    return requests.get(todo_url).json()


def export_to_csv(user_id):
    """
    Exports user's completed tasks to a CSV file.
    """
    user_data = get_user_data(user_id)
    username = user_data.get("username")

    user_todos = get_user_todos(user_id)
    completed_todos = [todo for todo in user_todos if todo.get('completed')]

    filename = f'{user_id}.csv'
    with open(filename, 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)

        for todo in user_todos:
            writer.writerow([
                        user_id,
                        username,
                        str(todo['completed']),
                        todo['title']
                        ])

    print(f"CSV data exported to {filename}")


def main():
    """Main function to execute the script."""
    user_id = sys.argv[1]
    export_to_csv(user_id)


if __name__ == "__main__":
    main()
