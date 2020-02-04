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
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos'
        )
    tasks = json.loads(todos.text)
    with open(
                "todo_all_employees.json",
                mode='w',
                encoding='utf-8') as f:

        for user in users:
                list_tasks_done = [] 
                for task in tasks:
                    json_task = collections.OrderedDict()
                    if(task.get('userId') == user.get('id')):
                        json_task['username'] = user.get('username')
                        json_task['task'] = task.get('title')
                        json_task['completed'] = task.get('completed')
                        list_tasks_done.append(json_task)
                user_json[user['id']] = list_tasks_done
        json.dump(user_json, f)
