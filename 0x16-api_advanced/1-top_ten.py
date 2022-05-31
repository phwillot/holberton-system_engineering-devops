#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    subreddit: subreddit to print titles
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}

    request = requests.get(url, headers=headers, allow_redirects=False)

    if request.status_code == 404:
        print(None)
    else:
        posts = request.json().get('data').get('children')
        for post in posts:
            print(post.get('data').get('title'))
