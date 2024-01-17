#!/usr/bin/python3
"""1-1-top_ten module"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given
    subreddit
    """
    BASE_URL = 'https://www.reddit.com'

    api_headers = {
        'Accept': 'application/json',
    }
    sort = 'top'
    limit = 10
    res = requests.get(
        '{}/r/{}/.json?sort={}&limit={}'.format(
            BASE_URL,
            subreddit,
            sort,
            limit
        ),
        headers=api_headers,
        allow_redirects=False
    )
    if res.status_code == 200:
        for post in res.json()['data']['children'][0:10]:
            print(post['data']['title'])
    else:
        print(None)
