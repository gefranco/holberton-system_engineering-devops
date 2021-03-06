#!/usr/bin/python3
'''
_____________________________________
get TODO from user in https://jsonplaceholder.typicode.com/
_____________________________________
'''
import json
import requests
import sys

if __name__ == "__main__":

    user_id = sys.argv[1]
    tasks_done = 0
    total_tasks = 0
    list_tasks_done = []
    request = requests.get('https://jsonplaceholder.typicode.com/users')
    users = json.loads(request.text)
    for user in users:
        if(int(user_id) == user['id']):
            request = requests.get(
                'https://jsonplaceholder.typicode.com/todos'
            )

            tasks = json.loads(request.text)
            for task in tasks:
                if(task.get('userId') == user.get('id')):
                    total_tasks += 1
                    if(task.get('completed')):
                        list_tasks_done.append(task.get('title'))
                        tasks_done += 1
            print(
                    "Employee " + user.get('name') +
                    " is done with tasks(" +
                    str(tasks_done) + "/" +
                    str(total_tasks) + "):")
            for task in list_tasks_done:
                print("\t " + task)
