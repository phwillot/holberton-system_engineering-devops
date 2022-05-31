#!/usr/bin/python3
"""
queries the Reddit API and returns the number of
subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    subreddit: subreddit to check the number of subscribers
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}

    request = requests.get(url, headers=headers, allow_redirects=False)

    if request.status_code == 404:
        return 0
    else:
        return request.json().get('data').get('subscribers')
