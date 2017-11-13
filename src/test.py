from constants import *
import json
import csv
from collections import Counter
import matplotlib.pyplot as plt

def checkForVerifiedUsers():
    with open(RATINGS_FILE) as f:
        ratings = json.load(f)
    # with open(VERIFIED_USERS) as f:
    #     users = json.load(f)
    
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

def generateTopUserGraphs():
    with open(TOPUSERS_FILE) as f:
        data = json.load(f)
    i = 0
    pts = []
    total = 0.0
    for u in data:
        i += 1
        total += u[1]
        if i%5 == 0:
            avg = total/i
            pts.append([i, avg])
    plt.plot(pts)
    plt.title("Average Adequacy of Top k Users")
    plt.ylabel('Adequacy')
    plt.xlabel('Top k')
    plt.savefig(PLOT_FILE)
    plt.close()



if __name__ == '__main__':
    # checkForVerifiedUsers()
    # ratingsToCsv()
    generateTopUserGraphs()
