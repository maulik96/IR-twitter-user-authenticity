import json
from os.path import dirname, realpath, join
from flask import Blueprint, request, render_template, jsonify
import shared_variables as var

routes_module = Blueprint('routes_module', __name__)
parent_dir_path = dirname(dirname(realpath(__file__)))
user_file = join(parent_dir_path, "data", "topUsers.json")
tuuser_file = join(parent_dir_path, "data", "topUsersOld.json")


@routes_module.route('/', methods=["GET"])
def homePage():
    if request.method == 'GET':
        with open(user_file) as f:
            data = json.load(f)
            users = [int(u[0]) for u in data]
        with open(tuuser_file) as f:
            data = json.load(f)
            users += [int(u[0]) for u in data]
        db = var.mongo.db
        print(len(users))
        users = db.twitusers.find({'user_id':{'$in' : users}})
        return render_template('home.html', users=users)


@routes_module.route('/tag/', methods=["POST"])
def tagUser():
    if request.method == 'POST':
        db = var.mongo.db
        user_handle = request.form["user_handle"]
        tag_value = request.form["tag_value"]
        res = db.twitusers.update_one(
            {"user_handle": user_handle},
            {"$set": {"manual_tag": tag_value}}
        )
        return jsonify({"user_handle": user_handle, "tag_value": tag_value})
