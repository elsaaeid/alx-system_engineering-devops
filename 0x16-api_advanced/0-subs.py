#!/usr/bin/python3
"""
Function that queries the Reddit API
and returns the number of subscribers
"""

from requests import get
from sys import argv


headers = {
    "User-Agent": "User-Agent",
    "X-Forwared-For": "iamsaid"
}


def number_of_subscribers(subreddit: str) -> int:
     """Queries the Reddit API if not
    a valid subreddit, return 0.
    """
    response = get("https://www.reddit.com/r/{}/about.json".format(subreddit),
                   headers=headers)
    data = response.json()
    try:
        if 'error' in data.keys():
            return 0
        else:
            return data['data']['subscribers']
    except Exception as e:
        return 0


if __name__ == "__main__":
    print(number_of_subscribers(argv[1]))
