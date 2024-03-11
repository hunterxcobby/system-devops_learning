import requests

def get_subreddit_info(subreddit_name):
    # Reddit API endpoint URL for getting information about a subreddit
    url = f"https://www.reddit.com/r/{subreddit_name}/about.json"

    # Set custom headers with user-agent to identify the application making the request
    headers = {"User-Agent": "My Reddit API Client"}

    # Make a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response into a Python dictionary
        subreddit_info = response.json()

        # Extract relevant information from the response
        subreddit_title = subreddit_info["data"]["display_name"]
        subreddit_subscribers = subreddit_info["data"]["subscribers"]
        subreddit_description = subreddit_info["data"]["public_description"]

        # Print the retrieved information
        print(f"Subreddit: {subreddit_title}")
        print(f"Subscribers: {subreddit_subscribers}")
        print(f"Description: {subreddit_description}")
    else:
        print(f"Failed to retrieve information. Status code: {response.status_code}")

# Example usage: Retrieve information about the "learnpython" subreddit
get_subreddit_info("learnpython")
