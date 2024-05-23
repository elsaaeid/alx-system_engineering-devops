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
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return None

    data = response.json()
    posts = data["data"]["children"]

    for post in posts:
        title = post["data"]["title"]
        hot_list.append(title)

    if "after" in data["data"]:
        after = data["data"]["after"]
        return recurse(subreddit, hot_list, after=after)

    return hot_list
