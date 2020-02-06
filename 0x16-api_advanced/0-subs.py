#!/usr/bin/python3
'''
___________________
module that contains the function number_of_subscribers(subreddit)
___________________
'''
import json
import requests
import sys


def number_of_subscribers(subreddit):
    '''
    queries the Reddit API and returns the number of subscribers
    '''
    try:
        request = requests.get(
            'https://www.reddit.com/r/'+sys.argv[1] + '/about.json',
            allow_redirects=False,
            headers={'User-agent': 'gefrancof'}
        )

        dictionary = json.loads(request.text)

        data = dictionary['data']
        return data['subscribers']
    except:
        return 0
