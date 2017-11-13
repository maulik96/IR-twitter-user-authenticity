import json
import numpy as np
from constants import *

weights = [0]*6
weights[RETWEET] = 0.4
weights[RETWEETED] = 0.0
weights[FOLLOW] = 0.4
weights[FOLLOWED] = 0.0
weights[POST] = 0.6
weights[POSTED] = 0.6

def newTweet():
    return {
        "pos": 0,
        RETWEETED: 0,
    }

def newUser(pos):
    return {
        "pos": pos,
        FOLLOW: 0,
        FOLLOWED: 0,
        POST: 0,
    }


def addRandomWeight(A, users, tweets):
    user_scores = [0]*len(users)
    tweet_scores = [0]*len(tweets)


    with open(FOLLOW_FILE) as f:
        followData = json.load(f)
    with open(RETWEET_FILE) as f:
        retweetData = json.load(f)
    import pudb; pudb.set_trace()
    for u in users:
        user_scores[users[int(u)].get("pos")] =  float(followData[str(u)]["followers"]**2)/ (followData[str(u)]["following"]+1)

    normaliseScores(user_scores)

    for t in tweets:
        tweet_scores[tweets[t].get("pos") -len(users)] = float(retweetData[str(t)])
    normaliseScores(tweet_scores)

    all_scores = user_scores + tweet_scores

    # print all_scores

    total = sum(all_scores)
    if total!=0:
        for score in all_scores:
            score/=total

    for i in range(len(A)):
        A[:,i] *= d
        A[:,i] +=(1-d)*all_scores[i]

    return A

def normaliseScores(a):
    nmax = max(a)
    nmin = min(a)

    for i in range(len(a)):
        a[i] -= nmin
    if nmax==nmin:
        return

    for i in range(len(a)):
        a[i] /= (nmax-nmin)


def normaliseWeights(graph, users, tweets):
    n = len(users)
    m = len(tweets)
    hsplit = np.split(graph, [n])
    (user_user, user_tweet, tweet_user, tweet_tweet) = (np.split(hsplit[0],[n], axis=1)[0], np.split(hsplit[0],[n], axis=1)[1], np.split(hsplit[1],[n], axis=1)[0], np.split(hsplit[1],[n], axis=1)[1])

    for u in users:
        i = users[u].get("pos")
        follow = users[u].get(FOLLOW)
        followed = users[u].get(FOLLOWED)
        post = users[u].get(POST)
        user_user[i] /= max(follow, 1)
        # user_user[:,i] /= max(followed, 1)
        user_tweet[i] /= max(post, 1)

    # for t in tweets:
    #     i = tweets[t].get("pos") - n
    #     retweeted = tweets[t].get(RETWEETED)
    #     tweet_tweet[:,i] /= max(retweeted, 1)


def buildGraph(tweetData, userData, users, tweets):
    n = len(users)
    m = len(tweets)
    A = np.zeros((n+m, n+m))

    for tw in tweetData:
        tweet = tw.get("id")
        user = tw.get("user_id")
        retweeted = tw.get("retweeted_status_id")
        u = users[user].get("pos")
        t = tweets[tweet].get("pos")
        A[u][t] = weights[POST]
        users[user][POST] += 1
        A[t][u] = weights[POSTED]
        if retweeted and tweets.get(retweeted):
            r = tweets[retweeted].get("pos")
            A[t][r] = weights[RETWEET]
            A[r][t] = weights[RETWEETED]
            tweets[retweeted][RETWEETED] += 1

    for user in userData:
        u = users[int(user)].get("pos")
        for following in userData[user]:
            f = users[following].get("pos")
            A[u.get("pos")][f.get("pos")] = weights[FOLLOW]
            users[user][FOLLOW] += 1
            A[f.get("pos")][u.get("pos")] = weights[FOLLOWED]
            users[following][FOLLOWED] += 1

    normaliseWeights(A, users, tweets)
    return addRandomWeight(A, users, tweets)


if __name__ == '__main__':
    with open(TWEET_DATAFILE) as f:
        tweetData = json.load(f)
    with open(USER_DATAFILE) as f:
        userData = json.load(f)
    users = {}
    tweets = {}
    i = 0
    j = 0
    for tweet in tweetData:
        tweets[tweet["id"]] = newTweet()
        if not users.get(tweet["user_id"]):
            users[tweet["user_id"]] = newUser(i)
            i += 1
        j += 1
    k = 0
    for tweet in tweets:
        tweets[tweet]["pos"] = i+k
        k += 1
    print("No. of tweets:", j)
    print("No. of users:", i)
    graph = buildGraph(tweetData, userData, users, tweets)
    np.save(MODEL_GRAPH_FILE, graph)
    with open(USER_DATA, "w") as f:
        json.dump(users, f)
