#!/usr/bin/python3
"""
2-export_to_json module
exports data to json
"""
import json
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
            user_name = user_res.get('username')
            todos = list(filter(lambda x: x.get('userId') == id, todos_res))
            with open('{}.json'.format(id), 'w') as file:
                for todo in todos:
                    file.write('"{}","{}","{}","{}"\n'.format(
                        id,
                        user_name,
                        todo['completed'],
                        todo['title']
                    ))
