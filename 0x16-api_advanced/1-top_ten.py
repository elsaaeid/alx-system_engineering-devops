#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles
of the first 10 hot posts for a given subreddit.
If the subreddit is invalid, it prints None.
"""

import requests


def top_ten(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'by u/Global_Finding_8439'}
    params = {
        "limit": 10
    }
    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data")
        [print(c.get("data").get("title")) for c in data.get("children")]
    else:
        print(None)

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        top_ten(subreddit)
