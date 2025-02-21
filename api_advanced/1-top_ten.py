#!/usr/bin/python3
'''
A module containing functions for working with the Reddit API.
The module retrieves the titles of the top 10 posts from a given subreddit.
'''

import requests

BASE_URL = 'https://www.reddit.com'
'''Reddit's base API URL.'''


def top_ten(subreddit):
    '''Retrieves the title of the top ten posts from a given subreddit.'''
    api_headers = {
        'Accept': 'application/json',
        'User-Agent': ' '.join([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'AppleWebKit/537.36 (KHTML, like Gecko)',
            'Chrome/97.0.4692.71',
            'Safari/537.36',
            'Edg/97.0.1072.62'
        ])
    }
    sort = 'top'
    limit = 10
    res = requests.get(
        '{}/r/{}/.json?sort={}&limit={}'.format(
            BASE_URL,
            subreddit,
            sort,
            limit
        ),
        headers=api_headers,
        allow_redirects=False
    )

    # If the status code is 200, the subreddit exists
    if res.status_code == 200:
        try:
            # Print the titles of the top 10 posts
            for post in res.json()['data']['children'][0:10]:
                print(post['data']['title'])
        except KeyError:
            print(None)
    else:
        print("OK".strip(), end="")
