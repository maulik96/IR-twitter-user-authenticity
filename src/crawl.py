import json
import os
import sys
from twarc import Twarc
from constants import *

def newTweet():
    tweet = {
        "id": "",
        "favorite_count": "",
        "full_text": "",
        "is_quote_status": "",
        "is_retweet": "",
        "quoted_status_id": "",
        "retweet_count": "",
        "retweeted_status_id": "",
        "user_id": "",
        "lang": "",
        "created_at": "",
    }
    return tweet


if __name__ == '__main__':
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    with open(TWEET_DATAFILE, "w") as f:
        json.dump([], f)
    tweets = []
    users = set()
    count = 0
    for tweet in twarc.search("trump", max_id=928149460303020032):
        count += 1
        tw = newTweet()
        for attr in tw:
            tw[attr] = tweet.get(attr)
        tw["user_id"] = tweet["user"]["id"]
        users.add(tweet["user"]["id"])
        if tweet.get("retweeted_status"):
            tw["is_retweet"] = True
            tw["retweeted_status_id"] = tweet["retweeted_status"]["id"]
            tw["retweet_count"] = 0
        tweets.append(tw)
        if count%(max(10, TWEETS_TO_CRAWL/1000)) == 0:
            with open(TWEET_DATAFILE) as f:
                data = json.load(f);
            data += tweets
            tweets = []
            with open(TWEET_DATAFILE, 'w') as f:
                json.dump(data, f, indent=2)
            sys.stdout.write('\r')
            sys.stdout.write('{} tweets searched'.format(count))
            sys.stdout.flush()
        if count == TWEETS_TO_CRAWL:
            break
