#!/usr/bin/python3
"""
queries the Reddit API and returns a list containing the titles of all hot
articles for a given subreddit.
If no results are found for the given subreddit, return None.
"""
import requests


def recurse(subreddit, after="", hot_list=[]):
    """
    subreddit: subreddit to get the titles of hot articles
    hot_list: list to push the titles
    """
    if after is None:
        return
    url = 'https://www.reddit.com/r/{}/hot.json?limit=100&after={}'.format(
        subreddit, after)
    headers = {'User-Agent': 'My User Agent 1.0'}

    request = requests.get(url, headers=headers, allow_redirects=False)

    if request.status_code == 404:
        return None
    else:
        posts = request.json().get('data').get('children')
        for post in posts:
            hot_list.append(post.get('data').get('title'))
            after = request.json().get('data').get('after')
        recurse(subreddit, after, hot_list)
        return hot_list
