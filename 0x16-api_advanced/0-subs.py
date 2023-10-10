#!/usr/bin/python3
"""returns number of subscribers for a subreddit"""

def number_of_queries(subreddit):
    """function that returns number of subscribers"""
    import requests

    sub_info = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code >= 300:
        return 0
    
    return sub_info.json().get("data").get("subscribers")
