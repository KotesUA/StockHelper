from datetime import date, timedelta

import requests
from keys import POLYGON_KEY

URL = "https://api.polygon.io/v1/open-close/"


def get_news(ticker):
    querystring = f"{URL}{ticker}/{date.today() - timedelta(days=1)}?apiKey={POLYGON_KEY}"
    print(querystring)
    response = requests.request("GET", querystring)
    if response.status_code != 200:
        print("Cannot get data (HTTP {}): {}".format(response.status_code, response.text))
    else:
        print(response.text)


if __name__ == "__main__":
    get_news("AAPL")
