#!/usr/bin/python3
'''
_____________________________________
get TODO from user in https://jsonplaceholder.typicode.com/
and Export to CSV
_____________________________________
'''
import csv
import json
import requests
import sys
if __name__ == "__main__":

    user_id = sys.argv[1]
    tasks_done = 0
    total_tasks = 0
    list_tasks_done = []
    rows_csv = []
    request = requests.get('https://jsonplaceholder.typicode.com/users')
    users = json.loads(request.text)
    for user in users:
        if(int(user_id) == user['id']):
            request = requests.get(
                'https://jsonplaceholder.typicode.com/todos'
            )

            tasks = json.loads(request.text)
            with open(user_id+".csv", mode='w', encoding='utf-8') as f:
                writer = csv.writer(f, quoting=csv.QUOTE_ALL)
                for task in tasks:
                    row_csv = ()
                    if(task.get('userId') == user.get('id')):
                        total_tasks += 1
                        row_csv = (
                            user.get('id'),
                            user.get('username'),
                            task.get('completed'),
                            task.get('title')
                        )
                        rows_csv.append(row_csv)
                writer.writerows(rows_csv)
