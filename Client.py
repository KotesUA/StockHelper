import json

import requests

URL = "https://127.0.0.1:500/"

if __name__ == "__main__":
    stats = requests.request("GET", f'{URL}stats?ticker=BTC')
    print(json.dumps(stats, indent=4, sort_keys=True))

    mood = requests.request("GET", f'{URL}mood?ticker=BTC')
    print(json.dumps(mood, indent=4, sort_keys=True))

    news = requests.request("GET", f'{URL}news?ticker=BTC')
    print(json.dumps(news, indent=4, sort_keys=True))
