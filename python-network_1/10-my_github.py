#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    # GitHub API URL to get user details
    url = "https://api.github.com/user"

    # Make the GET request with Basic Authentication
    response = requests.get(url, auth=(username, token))

    # Check if the response is successful
    if response.status_code == 200:
        # Parse the response JSON to get the user ID
        print(response.json().get("id"))
    else:
        print(None)

