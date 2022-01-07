import requests
from keys import yahoo_key

URL = "https://yfapi.net/v6/finance/quote"
HEADERS = {'x-api-key': f"{yahoo_key}"}


def get_news(ticker):
    querystring = {"symbols": f"{ticker}"}
    response = requests.request("GET", URL, headers=HEADERS, params=querystring)
    if response.status_code != 200:
        print("Cannot get data (HTTP {}): {}".format(response.status_code, response.text))
    else:
        print(response.text)


if __name__ == "__main__":
    get_news("AAPL")
