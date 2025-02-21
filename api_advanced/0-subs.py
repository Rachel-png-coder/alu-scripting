#!/usr/bin/python3
'''A module containing functions for working with the Reddit API.
'''

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Python/requests"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return 0

    try:
        results = response.json().get("data")
        if results:
            return results.get("subscribers", 0)
    except ValueError:
        return 0

    return 0
