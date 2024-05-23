#!/usr/bin/python3
"""
A recursive function that queries the Reddit API,
parses the titles of all hot articles, and counts
the occurrences of given keywords.
"""

import requests

def count_words(subreddit, word_list, after=None, count={}):
    """
    Prints the count of the given words present in
    the title of the subreddit's hottest articles.
    """
    if after is None:
        count = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "by u/Global_Finding_8439'"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    if "data" not in data or "children" not in data["data"]:
        return

    for post in data["data"]["children"]:
        title = post["data"]["title"].lower()
        for word in word_list:
            if word.lower() in title:
                count[word] = count.get(word, 0) + title.count(word.lower())

    if data["data"]["after"] is not None:
        count_words(subreddit, word_list, data["data"]["after"], count)
    else:
        sorted_count = sorted(count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_count:
            print(f"{word}: {count}")
