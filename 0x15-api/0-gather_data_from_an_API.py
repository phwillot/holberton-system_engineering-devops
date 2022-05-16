#!/usr/bin/python3
"""
Script that use an API to return information about
an employee about his/her TODO list progess
"""
import requests
from sys import argv

if __name__ == "__main__":
    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    username = user.json().get('name')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    listTodo = []
    counterOfTasksDone = 0
    totalTasks = 0

    for todo in todos.json():
        if todo.get('completed') \
                is True and str(todo.get('userId')) == argv[1]:
            counterOfTasksDone += 1
            listTodo.append(todo.get('title'))
        if str(todo.get('userId')) == argv[1]:
            totalTasks += 1

    print('Employee {} is done with tasks({}/{}):'.format(username,
          counterOfTasksDone, totalTasks))

    for todo in listTodo:
        print('\t {}'.format(todo))
