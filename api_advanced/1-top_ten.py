#!/usr/bin/python3
"""A module to query the Reddit API for hot posts."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed in a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    # Send a GET request to the subreddit URL
    res = requests.get(
        url, headers={"User -Agent": "Mozilla/5.0"}, allow_redirects=False
    )

    # Check if the request was successful
    if res.status_code != 200:
        print("OK")  # Print "OK" if the subreddit is invalid
        return

    # Parse the JSON response
    json_response = res.json()
    posts = json_response.get("data", {}).get("children", [])

    # Print the titles of the first 10 hot posts
    for post in posts:
        print(post.get("data", {}).get("title"))

# Test the function with the learnpython subreddit
top_ten("learnpython")  # This should print the titles of the top 10 posts

# Test the function with an invalid subreddit to see "OK"
top_ten("invalid_subreddit")  # This should print "OK"
