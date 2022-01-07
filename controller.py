import json
import time
import requests

from config import KEYWORDS, ACCOUNTS
from keys import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCES_KEY, TWITTER_ACCESS_SECRET, TWITTER_BEARER_TOKEN

search_url = "https://api.twitter.com/2/users"
search_term = 'NBA'
query_params = {'query': search_term, 'space.fields': 'title,created_at', 'expansions': 'creator_id'}


def tweet_checker(status):
    if any(word in status.text.lower() for word in KEYWORDS) and status.user.id_str in ACCOUNTS:
        print(f"Elon tweeted: {status.text} - on {time.ctime()}")


def create_headers(bearer_token):
    headers = {
        "Authorization": "Bearer {}".format(bearer_token),
        "User-Agent": "v2SpacesSearchPython"
    }
    return headers


def connect_to_endpoint(url, headers, params):
    response = requests.request("GET", search_url, headers=headers, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    headers = create_headers(TWITTER_BEARER_TOKEN)
    json_response = connect_to_endpoint(search_url, headers, query_params)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()