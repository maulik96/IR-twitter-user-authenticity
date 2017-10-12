from constants import *
import json
from collections import Counter

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
            count++
        print(u[0])
    print(count)

if __name__ == '__main__':
    checkForVerifiedUsers()
