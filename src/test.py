from constants import *
import csv


with open(USER_CSV, 'r') as f:
    reader = csv.reader(f)
    user_list = list(reader)

users = ""
for i in user_list:
	users += str(i[0]) + ","

i = 0
for user in twarc.user_lookup(users[:-1]):
	i += 1
	if user["verified"]:
		print(user["screen_name"])
	if(i%100 == 0):
		sys.stdout.write('\r')
		sys.stdout.write("Checked {} users.".format(i))
		sys.stdout.flush()

print("Checked {} users.".format(i))
# print(i)
