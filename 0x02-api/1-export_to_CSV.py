#!/usr/bin/python3
"""script to export data in the CSV format"""

import csv
import requests as res
from sys import argv


def getApi(u):
    """A function that returns to do list"""
    user = int(u)
    todo = res.get('https://jsonplaceholder.typicode.com/todos',
                   params={'userId': user}).json()
    empl = res.get('https://jsonplaceholder.typicode.com/users',
                   params={'id': user}).json()

    data_to_file = open(u+".csv", 'w', newline='')
    csv_writer = csv.writer(data_to_file, quoting=csv.QUOTE_NONNUMERIC)

    for i in range(0, len(todo)):
        todoList = todo[i]
        id = str(todoList['userId'])
        name = empl[0]['username']
        status = str(todoList['completed'])
        title = todoList['title']
        csv_writer.writerow([id, name, status, title])
    data_to_file.close()

if __name__ == '__main__':
    getApi(argv[1])
