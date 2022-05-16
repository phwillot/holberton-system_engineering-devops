#!/usr/bin/python3
"""
Same as task 0 but exports the result into CSV file
"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    username = user.json().get('username')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    with open('{}.csv'.format(argv[1]), 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos.json():
            if str(todo.get('userId')) == argv[1]:
                writer.writerow([argv[1], username, todo.get(
                    'completed'), todo.get('title')])
