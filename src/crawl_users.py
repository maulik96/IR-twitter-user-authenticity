import json
from constants import *


def crawlUserData(users):
    data = {}
    for user in users:
        following = []
        for friend in twarc.friend_ids(user):
            if friend in users:
                following.append(friend)
        data[user] = following
    with open(USER_DATAFILE, "w") as f:
        json.dump(data,f)

if __name__ == '__main__':

    users = set()
    with open(TWEET_DATAFILE) as f:
        tweets = json.load(f)

    for tw in tweets:
        users.add(tw.get('user_id'))
