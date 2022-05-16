#!/usr/bin/python3
"""
Same as task 0 but exports the result into JSON file
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    userId = argv[1]

    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    username = user.json().get('username')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    dictionary = {userId: []}

    for todo in todos.json():
        if str(todo.get('userId')) == userId:
            dictionary.get(userId).append({
                "task": todo.get('title'),
                "completed": todo.get('completed'),
                "username": username
            })

    with open('{}.json'.format(userId), "w") as jsonfile:
        jsonObject = json.dumps(dictionary, indent=4)
        jsonfile.write(jsonObject)
