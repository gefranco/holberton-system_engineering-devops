#!/usr/bin/python3
'''
'''
import json
import requests
import sys

def top_ten(subreddit):
    '''
    '''
    request = requests.get(
        'https://www.reddit.com/r/'+sys.argv[1] +
        '/top.json?limit=10&raw_json=1',
        allow_redirects=False,
        headers={'User-agent': 'gefrancof'}
    )
    if request.status_code != 200:
        print('None')
        return
    dictionary = request.json()
    data = dictionary['data']
    for data_index in data['children']:
        data_children = data_index['data']
        print(data_children['title'])
