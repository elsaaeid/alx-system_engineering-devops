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
    if subreddit is None or type(subreddit) is not str:
        return 0
    res = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)'}).json()
    subs_number = res.get("data", {}).get("subscribers", 0)
    return subs_number
