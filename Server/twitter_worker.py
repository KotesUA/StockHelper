import requests
from keys import TWITTER_BEARER_TOKEN

import requests
import os
import json


def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {TWITTER_BEARER_TOKEN}"
    r.headers["User-Agent"] = "StockHelperKotes"
    return r


def get_rules():
    response = requests.get("https://api.twitter.com/2/tweets/search/stream/rules", auth=bearer_oauth)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    print(json.dumps(response.json()))
    return response.json()


def delete_all_rules(rules):
    if rules is None or "data" not in rules:
        return None

    ids = list(map(lambda rule: rule["id"], rules["data"]))
    payload = {"delete": {"ids": ids}}
    response = requests.post("https://api.twitter.com/2/tweets/search/stream/rules", auth=bearer_oauth, json=payload)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    print(json.dumps(response.json()))


def set_rules(delete):
    sample_rules = [
        {"value": "dog has:images", "tag": "dog pictures"},
        {"value": "cat has:images -grumpy", "tag": "cat pictures"},
    ]
    payload = {"add": sample_rules}
    response = requests.post("https://api.twitter.com/2/tweets/search/stream/rules", auth=bearer_oauth, json=payload)
    if response.status_code != 201:
        raise Exception(response.status_code, response.text)
    print(json.dumps(response.json()))


def get_stream(set):
    response = requests.get("https://api.twitter.com/2/tweets/search/stream", auth=bearer_oauth, stream=True)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    for response_line in response.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            print(json.dumps(json_response, indent=4, sort_keys=True))


def main():
    rules = get_rules()
    delete = delete_all_rules(rules)
    set = set_rules(delete)
    get_stream(set)


if __name__ == "__main__":
    main()




def search_tweets(ticker):
    url = "https://api.twitter.com/2/tweets/search/recent"
    query_params = {
        'query': f'({ticker} -rich -free -miss -project) lang:en (bullish OR bearish)',
        'tweet.fields': 'author_id',
        'max_results': '100'
    }
    response = requests.request("GET", url, auth=bearer_oauth, params=query_params)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    else:
        return response.json()


def twitter_mood(ticker):
    feed = search_tweets(ticker)
    bulls = 0
    bears = 0
    for tweet in feed['data']:
        if "bull" in tweet["text"]:
            bears += 1
        else:
            if "bear" in tweet["text"]:
                bulls += 1
    return {'Ticker': ticker, 'Bulls': bulls, 'Bears': bears}
