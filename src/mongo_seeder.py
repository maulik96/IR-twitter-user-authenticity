from os.path import dirname, realpath, join
import json
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['twit_user_auth']

parent_dir_path = dirname(dirname(realpath(__file__)))
data_file = join(parent_dir_path, "data", "usernames.json")
# data_file = join(parent_dir_path, "sample_data", "usernames.json")

with open(data_file) as f:
    usernames = json.load(f)

docs = []
for x in usernames:
    doc = {
        "user_id": int(x),
        "user_handle": usernames[x],
        "authenticity_score": -1,
        "manual_tag": "untagged"
    }
    docs.append(doc)

db.twitusers.remove()
db.twitusers.insert(docs)
