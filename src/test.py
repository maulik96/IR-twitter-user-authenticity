from constants import *
import csv
import sys
import json

with open(USER_CSV, 'r') as f:
    reader = csv.reader(f)
    user_list = list(reader)

users = user_list.join(",")

i = 0
for user in twarc.user_lookup(users):
	i += 1
	usernames = {}
	print(user["id"])

	usernames[user["id"]] = user["screen_name"]
	with open(USERNAMES_FILE,"w") as f:
		json.dump(usernames,f)

	if user["verified"]:
		print(user["screen_name"])
	if(i%100 == 0):
		# sys.stdout.write('\r')
		sys.stdout.write("Checked {} users.".format(i))
		# sys.stdout.flush()

print("Checked {} users.".format(i))
# print(i)
