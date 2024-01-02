#!/usr/bin/python3
"""
0-0-gather_data_from_an_API module

"""
import re
import requests
from sys import argv

if __name__ == '__main__':
    if len(argv) > 1:
        if re.fullmatch(r'\d+', argv[1]):
            API_URL = 'https://jsonplaceholder.typicode.com/'
        id = int(argv[1])
        user_res = requests.get('{}/users/{}'.format(API_URL, id)).json()
        todos_res = requests.get('{}/todos'.format(API_URL)).json()
        user_name = user_res.get('name')
        todos = list(filter(lambda x: x.get('userId') == id, todos_res))
        todos_done = list(filter(lambda x: x.get('completed'), todos))
        print(
            'Employee {} is done with tasks({}/{}):'.format(
                user_name,
                len(todos_done),
                len(todos)
            )
        )
        for todo_done in todos_done:
            print('\t {}'.format(todo_done.get('title')))
