from constants import *
import json
import csv
from collections import Counter
import matplotlib.pyplot as plt
from pymongo import MongoClient

client = MongoClient('34.227.207.177', 27017)
db = client['twit_user_auth']


def checkForVerifiedUsers():
    with open(RATINGS_FILE) as f:
        ratings = json.load(f)
    with open(VERIFIED_USERS) as f:
        users = json.load(f)
    
    k = 25
    d = Counter(ratings)
        
    with open(TOPUSERS_FILE, "w") as f:
        json.dump(d.most_common(k), f)
  
    count = 0
    for u in d.most_common(k):
        if u[0] in users:
            count+=1
        print(u[0])
    print(count)

def ratingsToCsv():
    with open(RATINGS_FILE) as f:
        data = json.load(f)
    ratings = [["User", "Rating"]]
    for u in data:
        ratings.append([u, data[u]])
    with open(RATINGS_CSV, "w") as f:
        writer = csv.writer(f)
        writer.writerows(ratings)

def getPoints(users):
    total = 0.0
    x,y = [],[]
    i = 0
    for u in users:
        i += 1
        tag = db.twitusers.find_one({'user_id':u}).get("manual_tag")
        print(str(u) + " " + tag)
        if tag == "yes":
            rating = 1.0
        elif tag == "no":
            rating = 0.0
        else:
            rating = 0.5
        total += rating
        if i%5 == 0:
            avg = total/i
            x.append(i)
            y.append(avg)
    return x,y

def generateTopUserGraphs():
    with open(TOPUSERS_FILE) as f:
        data = json.load(f)
    print("Getting data points for our method")
    x,y = getPoints([int(u[0]) for u in data])
    line1, = plt.plot(x,y, '-o', label='Our method')
    with open(TOPUSERS_OLD_FILE) as f:
        data = json.load(f)
    print("Getting data points for TU rank")
    x,y = getPoints([int(u[0]) for u in data])
    line2, = plt.plot(x,y, '-o', label='TU Rank')
    
    plt.legend(handles=[line1, line2])
    plt.title("Average Adequacy of Top k Users")
    plt.ylabel('Adequacy')
    plt.xlabel('Top k')
    plt.savefig(PLOT_FILE)
    plt.close()



if __name__ == '__main__':
    checkForVerifiedUsers()
    ratingsToCsv()
    # generateTopUserGraphs()
