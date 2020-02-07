#!/usr/bin/python3
'''
___________________
module that contains recurse(subreddit, hot_list=[]): function
___________________
'''
import requests
import sys


def recurse(subreddit, hot_list=[]):
    '''
    return the first number of hot posts listed for a given subreddit.
    '''
    after = None
    request = None
    if len(subreddit.split("|")) > 1:
        after = subreddit.split("|")[1]
        request = requests.get(
            'https://www.reddit.com/r/' + subreddit.split("|")[0] +
            '/hot.json?after='+subreddit.split("|")[1],
            allow_redirects=False,
            headers={'User-agent': 'gefrancof'}
        )
    else:
        request = requests.get(
            'https://www.reddit.com/r/' + subreddit +
            '/hot.json',
            allow_redirects=False,
            headers={'User-agent': 'gefrancof'}
        )
    if request.status_code == 200:

        dictionary = request.json()

        data = dictionary['data']

        if data["after"] is None:
            return hot_list
        else:
            for data_index in data['children']:
                data_children = data_index['data']
                hot_list.append(data_children['title'])
            return recurse(
                         subreddit.split("|")[0] +
                         "|" + data["after"],
                         hot_list)
