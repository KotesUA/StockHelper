import requests
import json
from keys import TWITTER_BEARER_TOKEN


def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {TWITTER_BEARER_TOKEN}"
    r.headers["User-Agent"] = "StockHelperKotes"
    return r


def search_tweets(ticker):
    url = "https://api.twitter.com/2/tweets/search/recent"
    query_params = {
        'query': f'({ticker} -rich -free -miss -project) lang:en (bullish OR bearish)',
        'tweet.fields': 'author_id',
        'max_results': '100'
    }
    response = requests.request("GET", url, auth=bearer_oauth, params=query_params)
    if response.status_code != 200:
        print("Request returned an error: {} {}".format(response.status_code, response.text))
    else:
        return response.json()


def mood(ticker):
    feed = search_tweets(ticker)
    bulls = 0
    bears = 0
    for tweet in feed['data']:
        if "bull" in tweet["text"]:
            bears += 1
        else:
            if "bear" in tweet["text"]:
                bulls += 1
    return bulls, bears


if __name__ == "__main__":
    ticker = 'BTC'
    print(json.dumps(search_tweets(ticker), indent=4, sort_keys=True))
    bulls, bears = mood(ticker)
    print(f'Twitter mood for {ticker}:\n\tBulls: {bulls}\n\tBears: {bears}')
