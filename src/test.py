from constants import *
import json

def checkForVerifiedUsers():
    with open(RATINGS_FILE) as f:
        ratings = json.load(f)
    with open(VERIFIED_USERS) as f:
        users = json.load(f)
    for u in users:
        print(ratings[u])

if __name__ == '__main__':
    checkForVerifiedUsers()
