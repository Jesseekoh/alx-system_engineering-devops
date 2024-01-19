#!/usr/bin/python3
"""0-subs.py module"""
import requests


def number_of_subscribers(subreddit):
    """Gets the number of subscribers a subreddit has"""
    BASE_URL = 'https://www.reddit.com'

    api_headers = {
        'Accept': 'application/json',
        'User-Agent': ' '.join([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'AppleWebKit/537.36 (KHTML, like Gecko)',
            'Chrome/97.0.4692.71',
            'Safari/537.36',
            'Edg/97.0.1072.62'
        ])
    }
    res = requests.get(
        '{}/r/{}/about/.json'.format(BASE_URL, subreddit),
        allow_redirects=False,
        headers=api_headers
    )

    if res.status_code == 200:
        data = res.json()
        return data['data']['subscribers']
    return 0
