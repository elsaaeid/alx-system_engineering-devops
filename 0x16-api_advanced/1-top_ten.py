#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Function that queries the Reddit API 
    if not a valid subreddit, print None.
    """
    try:
        base_url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
        headers = {'User-agent': 'Custom'}
        response = requests.get(base_url, headers=headers)
        data = response.json()
        
        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            for post in posts:
                title = post['data']['title']
                print(title)
        else:
            print("None")
    except:
        print("None")
