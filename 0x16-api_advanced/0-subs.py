#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of total subscribers for a given
subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Funtion that queries the Reddit API.
    """
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'custom'}
    response = requests.get(url, headers=headers)
    if response.status_code >= 300:
        return 0
    subscriber_count = response.json().get('data').get('subscribers')
    return subscriber_count
