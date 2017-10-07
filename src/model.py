import json
from constants import *

def newTweet(pos):
    return {
        "pos" : pos,
        RETWEETED: 0,
    } 

def newUser(pos):
    return {
        "pos" : pos,
        FOLLOW: 0,
        FOLLOWED: 0,
        POST: 0,
    } 

# def buildGraph(data, users, tweets):
    

if __name__ == '__main__':
    with open(DATA_FILE) as f:
        data = json.load(f)
    users = {}
    tweets = {}
    i = 0
    j = 0
    for tweet in data:
        tweets[tweet["id"]] = newTweet(i)
        if not users.get(tweet["user_id"]):
            users[tweet["user_id"]] = newUser(j)
            j += 1
        i += 1
    print("No. of tweets:", i)
    print("No. of users:", j)
    # buildGraph(data, users, tweets)
