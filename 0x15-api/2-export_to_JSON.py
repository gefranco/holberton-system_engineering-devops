#!/usr/bin/python3
'''
_____________________________________
get TODO from user in https://jsonplaceholder.typicode.com/
and Export to JSON
_____________________________________
'''
import collections
import json
import requests
import sys
if __name__ == "__main__":

    user_id = sys.argv[1]
    list_tasks_done = []
    json_task = collections.OrderedDict()
    rows_csv = []
    user_json = {}
    request = requests.get('https://jsonplaceholder.typicode.com/users')
    users = json.loads(request.text)
    for user in users:
        if(int(user_id) == user.get('id')):
            request = requests.get(
                'https://jsonplaceholder.typicode.com/todos'
            )

            tasks = json.loads(request.text)
            with open(user_id+".json", mode='w', encoding='utf-8') as f:
                for task in tasks:
                    if(task.get('userId') == user.get('id')):
                        json_task['task'] = task.get('title')
                        json_task['completed'] = task.get('completed')
                        json_task['username'] = user.get('username')
                        list_tasks_done.append(json_task)
                user_json[user['id']] = list_tasks_done
                json.dump(user_json, f)
