#!/usr/bin/env python3

import requests

def fetch_user_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    repositories = []

    while url:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            repositories.extend(data)
            # Check if there's a next page
            url = response.links.get('next', {}).get('url')
        else:
            print(f"Failed to fetch repositories: {response.status_code}")
            break

    return repositories

# Example usage
username = "hunterxcobby"
user_repositories = fetch_user_repositories(username)
print(f"Total repositories for {username}: {len(user_repositories)}")
