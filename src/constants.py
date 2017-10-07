from os.path import dirname, realpath, join, exists

TWEETS_TO_CRAWL = 10
DATA_DIR = join(dirname(dirname(realpath(__file__))), "data")
DATA_FILE = join(DATA_DIR, "search.json")

RETWEET = 1
RETWEETED = 2
FOLLOW = 3
FOLLOWED = 4
POST = 5
POSTED = 6
