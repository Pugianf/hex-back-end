#!/usr/bin/python3
"""script to export data in the JSON format"""

import json
import requests as res
from sys import argv


def getApi(u):
    """A function that returns to do list in JSON"""
    user = int(u)
    todo = res.get('https://jsonplaceholder.typicode.com/todos',
                   params={'userId': user}).json()
    empl = res.get('https://jsonplaceholder.typicode.com/users',
                   params={'id': user}).json()
    todoList = []
    filename = open(u+".json", 'w')
    for i in range(len(todo)):
        line = {
            "task": todo[i]['title'],
            "completed": todo[i]['completed'],
            "username": empl[0]['username']
        }
        todoList.append(line)
        todoDict = {u: todoList}
    json.dump(todoDict, filename)

if __name__ == '__main__':
    getApi(argv[1])
