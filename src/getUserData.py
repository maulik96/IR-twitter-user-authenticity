from constants import *
import csv
import sys
import json


with open(USER_CSV, 'r') as f:
    reader = csv.reader(f)
    user_list = list(reader)

user_list = [u[0] for u in user_list]

i = 0
verified = {}
usernames = {}
follow = {}

for user in twarc.user_lookup(user_ids=user_list):
    i += 1
    usernames[user["id"]] = user["screen_name"]
    followers = user["followers_count"]
    following = user["friends_count"]
    follow[user["id"]] = {
        "followers" : followers,
        "following" : following,
    }
    if user["verified"]:
        verified[user["id"]] = user["screen_name"]
        print(user["screen_name"])
    
    if(i%100 == 0 or len(user_list)-i < 100):
        # sys.stdout.write('\r')
        sys.stdout.write("Checked {} users.\n".format(i))
        # sys.stdout.flush()
        with open(USERNAMES_FILE,"w") as f:
            json.dump(usernames,f)
        with open(FOLLOW_FILE,"w") as f:
            json.dump(follow,f)

with open(VERIFIED_USERS,"w") as f:
    json.dump(verified,f)

with open(USERNAMES_FILE,"w") as f:
    json.dump(usernames,f)

print("Checked {} users.".format(i))
print("Total {}  verified users.".format(len(verified)))
