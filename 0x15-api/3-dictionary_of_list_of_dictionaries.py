#!/usr/bin/python3
"""
Same as task 2 but get all the users into JSON file
"""
import json
import requests

if __name__ == "__main__":
    dictionary = {}

    users = requests.get(
        'https://jsonplaceholder.typicode.com/users/')

    for user in users.json():
        dictionary[user.get('id')] = []

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    for todo in todos.json():
        username = ""
        for user in users.json():
            if todo.get('userId') == user.get('id'):
                username = user.get('username')
        dictionary.get(todo.get('userId')).append({
            'username': username,
            'task': todo.get('title'),
            'completed': todo.get('completed')
        })

    with open('todo_all_employees.json', "w") as jsonfile:
        jsonObject = json.dumps(dictionary, indent=4)
        jsonfile.write(jsonObject)
