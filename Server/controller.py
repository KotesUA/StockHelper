from flask import Flask, request, abort
from twitter_worker import search_tweets, twitter_mood
from yahoo_worker import get_news
from polygon_worker import get_stats

app = Flask(__name__)


@app.errorhandler(404)
def ticker_not_found(error):
    return "This ticker is not available.", 404


@app.errorhandler(503)
def ticker_not_found(error):
    return "This service is not available.", 503


@app.route("/news")
def news():
    ticker = request.args.get("ticker")
    try:
        news = search_tweets(ticker)
        return news
    except Exception as e:
        if e.args[0] == 404:
            abort(404)
        else:
            abort(503)


@app.route("/mood")
def mood():
    ticker = request.args.get("ticker")
    try:
        mood = twitter_mood(ticker)
        return mood
    except Exception as e:
        if e.args[0] == 404:
            abort(404)
        else:
            abort(503)


@app.route("/stats")
def stats():
    ticker = request.args.get("ticker")
    try:
        stats = get_stats(ticker)
        return stats
    except Exception as e:
        if e.args[0] == 404:
            abort(404)
        else:
            abort(503)


if __name__ == "__main__":
    app.run()
