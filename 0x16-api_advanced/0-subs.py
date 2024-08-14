#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
    
    Returns:
        int: The number of subscribers for the subreddit, or 0 if the subreddit is invalid.
    """
    # Reddit API URL for the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Custom User-Agent to avoid Too Many Requests errors
    headers = {
        'User-Agent': 'python:subreddit.subscriber.count:v1.0 (by /u/yourusername)'
    }
    
    # Make the GET request
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Return the number of subscribers
        return data.get('data', {}).get('subscribers', 0)
    else:
        # If subreddit is invalid or request failed, return 0
        return 0

