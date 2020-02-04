#!/usr/bin/python3
'''
_____________________________________
get TODO from all users in https://jsonplaceholder.typicode.com/
and Export to JSON
_____________________________________
'''
import collections
import json
import requests
import sys
if __name__ == "__main__":

    tasks_done = 0
    total_tasks = 0
    list_tasks_done = []
    json_task = {}
    rows_csv = []
    user_json = {}
    request = requests.get('https://jsonplaceholder.typicode.com/users')
    users = json.loads(request.text)
    for user in users:
        if(True):
            request = requests.get(
                'https://jsonplaceholder.typicode.com/todos'
            )

            tasks = json.loads(request.text)
            with open(
                        "todo_all_employees.json",
                        mode='w',
                        encoding='utf-8') as f:
                for task in tasks:
                    row_csv = ()
                    if(task.get('userId') == user.get('id')):
                        json_task = collections.OrderedDict()
                        json_task['task'] = task.get('title')
                        json_task['completed'] = task.get('completed')
                        json_task['username'] = user.get('username')
                        list_tasks_done.append(json_task)
                    user_json[user['id']] = list_tasks_done
                json.dump(user_json, f)
