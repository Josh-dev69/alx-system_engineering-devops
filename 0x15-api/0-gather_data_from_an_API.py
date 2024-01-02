#!/usr/bin/python3

"""

This script retrieves information about a user and their
completed tasks from the JSONPlaceholder API.

Usage:
    python3 0-gather_data_from_an_API.py <user_id>
"""

from requests import get
from sys import argv


def get_employee_data(employee_id):
    """
        Fetches employee data and todo list from the given REST API
    """
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    return get(url).json()


def get_todo_list(employee_id):
    """
        Fetches the todo list of the employee from the given REST API.
    """
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    return get(url).json()


def display_todo_progress(employee_data, todo_list):
    """
        Displays the employee TODO list progress in the specified format.
    """
    employee_name = employee_data.get("name")
    completed_todos = []
    for todo in todo_list:
        if todo.get('completed'):
            completed_todos.append(todo)
    total = len(todo_list)
    completed = len(completed_todos)

    print(f"Employee {employee_name} is done with tasks({completed}/{total}):")

    for todo in completed_todos:
        print(f"     {todo['title']}")


if __name__ == "__main__":
    employee_id = int(argv[1])

    employee_data = get_employee_data(employee_id)
    todo_list = get_todo_list(employee_id)

    display_todo_progress(employee_data, todo_list)
