#!/usr/bin/python3
'''
'''
import requests
import json
import sys


def number_of_subscribers(subreddit):
    '''
    '''
    try:
        request = requests.get(
            'https://www.reddit.com/r/'+sys.argv[1] + '/about.json',
            headers={'User-agent': 'gefrancof'}
        )

        dictionary = json.loads(request.text)

        data = dictionary['data']
        return data['subscribers']
    except:
        return 0
