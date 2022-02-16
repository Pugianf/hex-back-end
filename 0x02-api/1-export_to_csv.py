#!/usr/bin/python3
"""script that export data in the CSV format"""

import csv
import requests as res
from sys import argv


def export_csv(u):
    """A function that exports a csv"""
    user = int(u)
    todo = res.get('https://jsonplaceholder.typicode.com/todos',
                   params={'userId': user}).json()
    emp = res.get('https://jsonplaceholder.typicode.com/users',
                  params={'id': user}).json()

    data_to_file = open('{}.csv'.format(u), 'w', newline='')
    csv_writer = csv.writer(data_to_file, quoting=csv.QUOTE_ALL)

    for i in range(0, len(todo)):
        todoList = todo[i]
        id = user
        name = emp[0]['username']
        status = str(todoList['completed'])
        title = todoList['title']
        csv_writer.writerow([id, name, status, title])
    data_to_file.close()

if __name__=='__main__':
    export_csv(argv[1])

