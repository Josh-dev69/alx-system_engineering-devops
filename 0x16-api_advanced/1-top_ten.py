#!/usr/bin/python3
""" getting top 10 hot topic of a subreddits """
import requests


def top_ten(subreddit):
    """ getting top 10 hot topic of a subreddits """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'your_user_agent'}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(None)
        return

    try:
        data = response.json()
    except ValueError:
        print("None")
        return

    if 'data' not in data or 'children' not in data['data']:
        print("None")
        return

    posts = data['data']['children']

    for post in posts:
        print(post['data']['title'])
