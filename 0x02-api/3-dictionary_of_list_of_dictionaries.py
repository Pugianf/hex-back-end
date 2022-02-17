#!/usr/bin/python3
"""script to export data in the JSON format"""

import json
import requests as res


def getApi():
    """A function that returns to do list"""
    empl = res.get('https://jsonplaceholder.typicode.com/users').json()
    todoDict = {}
    filename = open("todo_all_employees.json", 'w')
    for i in range(len(empl)):
        id = empl[i]['id']
        todo = res.get('https://jsonplaceholder.typicode.com/todos',
                       params={'userId': id}).json()
        todoList = []
        for j in range(len(todo)):
            line = {
                "task": todo[j]['title'],
                "completed": todo[j]['completed'],
                "username": empl[i]['username']
            }
            todoList.append(line)
        todoDict.update({id: todoList})
    return json.dump(todoDict, filename)

if __name__ == '__main__':
    getApi()
