from os.path import dirname, realpath, join
import json
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['twit_user_auth']

parent_dir_path = dirname(dirname(realpath(__file__)))
user_file = join(parent_dir_path, "data", "usernames.json")
ratings_file = join(parent_dir_path, "data", "ratings.json")
verified_file = join(parent_dir_path, "data", "verified.json")

with open(user_file) as f:
    usernames = json.load(f)
with open(ratings_file) as f:
    ratings = json.load(f)
with open(verified_file) as f:
    verified = json.load(f)


def db_init():
    docs = []
    for x in usernames:
        rating = ratings[x]
        ver_user = 0
        if x in verified:
            ver_user = 1
        doc = {
            "user_id": int(x),
            "user_handle": usernames[x],
            "authenticity_score": rating,
            "manual_tag": "untagged",
            "verified": ver_user
        }
        docs.append(doc)

    db.twitusers.remove()
    db.twitusers.insert(docs)


def db_verify():
    db.twitusers.update_many({"verified":1}, {"$set":{"manual_tag":"yes"}})


db_init()
db_verify()
