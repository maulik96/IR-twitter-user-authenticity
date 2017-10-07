import json
import sys
from twarc import Twarc
from constants import *

t = Twarc("22GyvUC4Jg89Eh1PuKRh3mwRo", 
          "m75gOSwIccfzYLWxwMCpHEldxgzYP83pTOSqAFbumQ5B6OF1vC",
          "852540250467467266-NoSAf6ZXmWZnr01CdUIfYBP5Z4cLZGJ",
          "kWP6L9F4YCUAsvwuaruuCUPMc4JqAE2jhJA8bhuuQSCSu")

def getNewTweet():
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
    with open(DATA_FILE, "w") as f:
        json.dump([], f)
    tweets = []
    count = 0
    for tweet in t.search("trump"):
        count += 1
        tw = getNewTweet()
        for attr in tw:
            tw[attr] = tweet.get(attr)
        tw["user_id"] = tweet["user"]["id"]
        if tweet.get("retweeted_status"):
            tw["is_retweet"] = True
            tw["retweeted_status_id"] = tweet["retweeted_status"]["id"]
        tweets.append(tw)
        if count%(TWEETS_TO_CRAWL/10) == 0:
            with open(DATA_FILE) as f:
                data = json.load(f);
            data += tweets
            tweets = []
            with open(DATA_FILE, 'w') as f:
                json.dump(data, f, indent=2)
            sys.stdout.write('\r')
            sys.stdout.write('{} tweets searched'.format(count))
            sys.stdout.flush()
        if count == TWEETS_TO_CRAWL:
            break
