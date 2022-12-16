#!/usr/bin/python3
"""script that takes your GitHub credentials (username and password) and uses
the GitHub API to display your id"""

if __name__ == '__main__':
    import sys
    import requests

    url = 'https://api.github.com/user'
    payload = {'login': sys.argv[1]}
    response = requests.get(url, params=payload, auth=(
        sys.argv[1], sys.argv[2])).json()

    try:
        print(response['id'])
    except KeyError:
        print('None')
