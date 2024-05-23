#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None.
"""

import requests

def recurse(subreddit, hot_list=[]):
    """
    Queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit.
    If not a valid subreddit, return None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "by u/Global_Finding_8439'"}
    params = [
        "after": after,
        "count": count,
        "limit": 100
    ]
    response = requests.get(url,
        headers=headers,
        params=params,
        allow_redirects=False)

    if response.status_code == 404:
        return None

    data = response.json().get("data")
        after = data.get("after")
        count += data.get("dist")
        for c in data.get("children"):
            hot_list.append(c.get("data").get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, after, count)
        return hot_list
