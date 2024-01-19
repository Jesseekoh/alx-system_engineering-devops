#!/usr/bin/python3
"""2-2-recurse module"""
import requests


def recurse(subreddit, hot_list=[]):
    """A recursive funtion that returns a list containing
    the titles of all hot articles for a given subreddit"""
    BASE_URL = 'https://www.reddit.com'
    res = requests.get(
        '{}/'
    )
