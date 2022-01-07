from datetime import date, timedelta
import requests
from keys import POLYGON_KEY


def get_stats(ticker):
    url = "https://api.polygon.io/v1/open-close/"
    querystring = f"{url}{ticker}/{date.today() - timedelta(days=1)}?apiKey={POLYGON_KEY}"
    response = requests.request("GET", querystring)

    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    else:
        return response.json()
