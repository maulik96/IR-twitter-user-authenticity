from os.path import dirname, realpath, join, exists
from twarc import Twarc


twarc = Twarc("22GyvUC4Jg89Eh1PuKRh3mwRo", 
          "m75gOSwIccfzYLWxwMCpHEldxgzYP83pTOSqAFbumQ5B6OF1vC",
          "852540250467467266-NoSAf6ZXmWZnr01CdUIfYBP5Z4cLZGJ",
          "kWP6L9F4YCUAsvwuaruuCUPMc4JqAE2jhJA8bhuuQSCSu")

TWEETS_TO_CRAWL = 1000
DATA_DIR = join(dirname(dirname(realpath(__file__))), "data")
TWEET_DATAFILE = join(DATA_DIR, "tweets.json")
USER_DATAFILE = join(DATA_DIR, "users.json")

RETWEET = 0
RETWEETED = 1
FOLLOW = 2
FOLLOWED = 3
POST = 4
POSTED = 5
