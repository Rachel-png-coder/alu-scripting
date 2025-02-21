#!/usr/bin/python3
"""A module to query the Reddit API for hot posts."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed in a subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None: Prints "None" if subreddit is invalid or request fails.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    # Send request with no redirects allowed
    res = requests.get(url, headers=headers, allow_redirects=False)

    # If request fails (invalid subreddit or other error)
    if res.status_code != 200:
        print("None")
        return

    try:
        # Extract post data from JSON response
        json_response = res.json()
        posts = json_response.get("data", {}).get("children", [])

        if not posts:
            print("None")
            return

        # Print the titles of the first 10 hot posts
        for post in posts:
            print(post.get("data", {}).get("title", "None"))

    except ValueError:
        print("None")
