#!/usr/bin/python3
'''
___________________
module that contains def top_ten(subreddit) function
___________________
'''
import json
import requests
import sys


def top_ten(subreddit):
    '''
    return the first 10 hot posts listed for a given subreddit.
    '''
    request = requests.get(
        'https://www.reddit.com/r/' + subreddit +
        '/hot.json?limit=10',
        headers={'User-agent': 'gefrancof'}
    )
    if request.status_code != 200:
        print(None)
        return
    dictionary = request.json()
    data = dictionary['data']
    for data_index in data['children']:
        data_children = data_index['data']
        print(data_children['title'])
