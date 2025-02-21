#!/usr/bin/python3
"""
Script to print hot posts on a given Reddit subreddit.
"""

import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    # Construct the URL for the subreddit's hot posts in JSON format
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # Define headers for the HTTP request, including User-Agent
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # Define parameters for the request, limiting the number of posts to 10
    params = {
        "limit": 10
    }

    # Send a GET request to the subreddit's hot posts page
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Check if the request was unsuccessful or returned empty content
    if response.status_code != 200:
        print("None")
        return

    try:
        # Parse the JSON response and extract the 'data' section
        json_data = response.json()
        results = json_data.get("data", {})
        children = results.get("children", [])

        # Print the titles of the top 10 hottest posts
        if children:
            for post in children[:10]:
                title = post.get("data", {}).get("title")
                if title:
                    print(title)
                else:
                    print("None")
        else:
            print("None")
    except (ValueError, KeyError):
        print("None")

