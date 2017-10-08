import json
import sys
from constants import *


def crawlUserData(users):
    print("Crawling user data...")
    with open(USER_DATAFILE, "w") as f:
        json.dump({}, f)
    data = {}
    count = 0
    n = len(users)
    for user in users:
        following = []
        count += 1
        for friend in twarc.friend_ids(user):
            if friend in users:
                following.append(friend)
        data[user] = following
        if count == n or count%10 == 0:
            with open(USER_DATAFILE) as f:
                storedData = json.load(f)
            storedData.update(data)
            with open(USER_DATAFILE, 'w') as f:
                json.dump(storedData, f)
            data = {}
            sys.stdout.write('\r')
            sys.stdout.write('{} users crawled. {}% done'.format(count, (count*100.0)/n))
            sys.stdout.flush()

if __name__ == '__main__':

    users = set()
    with open(TWEET_DATAFILE) as f:
        tweets = json.load(f)

    for tw in tweets:
        users.add(tw.get('user_id'))

    crawlUserData(users)
