from constants import *
import csv
import json

with open(TWEET_DATAFILE) as f:
	data = json.load(f)

tweets = []
users = set()
for tweet in data:
	tweets.append([tweet["id"]])
	users.add(tweet["user_id"])

users = [[u] for u in users]

with open(TWEETs_CSV, "w") as f:
    writer = csv.writer(f)
    writer.writerows(tweets)

with open(USER_CSV, "w") as f:
    writer = csv.writer(f)
    writer.writerows(users)

relations = [[":START_ID(User)",":END_ID(Tweet)",":TYPE"]]
with open(USER_TWEET_CSV, "w") as f:
	for tweet in data:
		relations.append([tweet["user_id"], tweet["id"], "Post"])
		relations.append([tweet["id"], tweet["user_id"], "Posted"])
	writer = csv.writer(f)
	writer.writerows(relations)

relations = [[":START_ID(Tweet)",":END_ID(Tweet)",":TYPE"]]
tweets = set([i[0] for i in tweets])
with open(TWEET_TWEET_CSV, "w") as f:
	for tweet in data:
		if(tweet["is_retweet"] is True):
			retweetId = tweet["retweeted_status_id"]
			if retweetId in tweets:
				relations.append([tweet["id"], retweetId, "Retweet"])
				relations.append([retweetId, tweet["id"], "Retweeted"])
	writer = csv.writer(f)
	writer.writerows(relations)

