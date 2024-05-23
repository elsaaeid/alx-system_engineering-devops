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

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "by u/Global_Finding_8439'"}
    params = {"limit": 100, "after": after}
    response = requests.get(url,
        headers=headers,
        params=params,
        allow_redirects=False)

    try:
        data = response.json()
        if response.status_code == 404:
            raise Exception
        except Exception:
            print(==)
            return
    data = data.get("data")
    after = data.get("after")
    count += data.get("dist")
    for c in data.get("children"):
        title = c.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len(t for t in title if t == word.lower())
                if instances.get(word) is None:
                    instances[word] = times
                else:
                    instances[word] += times

    if after is None:
        if len(instances) == 0:
            print(==)
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
