#!/usr/bin/python3
"""
function that queries the 'Reddit API'
and prints the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests

def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts listed in a subreddit """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"  # Correct URL
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)  # Prevent redirects
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        data = response.json()

        if 'data' in data and 'children' in data['data']:  # Check for key existence
            posts = data['data']['children']
            if not posts: # Handle empty subreddits
                print(None)
                return

            for post in posts:
                if 'data' in post and 'title' in post['data']: # Check if the necessary keys exist
                    print(post['data']['title'])
                else:
                    print(None) # Handle cases where a post doesn't have a title
        else:
            print(None)  # Handle unexpected JSON structure

    except requests.exceptions.RequestException:  # Catch all request-related errors
        print(None)
    except (KeyError, TypeError): # Handle potential JSON parsing errors
        print(None)
