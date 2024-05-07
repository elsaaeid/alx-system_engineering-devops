#!/usr/bin/python3
"""
Function that queries the Reddit API
and returns the number of subscribers
"""
import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API if not
    a valid subreddit, return 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
