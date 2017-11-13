from constants import *
import json

with open(TWEET_DATAFILE) as f:
	tweets = json.load(f)

ids = [str(t["id"]) for t in tweets]

retweets = {}
for tw in tweets:
	retweets[tw["id"]] = tw["retweet_count"]

with open(RETWEET_FILE, "w") as f:
	json.dump(retweets, f)
