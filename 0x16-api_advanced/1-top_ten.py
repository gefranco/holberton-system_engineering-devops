#!/usr/bin/python3
'''
'''
import json
import requests
import sys


def top_ten(subreddit):
    '''
    '''
    try:
        request = requests.get(
            'https://www.reddit.com/r/'+sys.argv[1] +
            '/top.json?limit=10&raw_json=1',
            headers={'User-agent': 'gefrancof'}
        )

        dictionary = json.loads(request.text)

        data = dictionary['data']
        for data_index in data['children']:
            data_children = data_index['data']
            title = data_children['title']

            print(title)

    except Exception as e:
        print(e)
        return 0
