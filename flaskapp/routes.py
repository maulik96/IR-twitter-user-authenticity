from flask import Blueprint, request, render_template, jsonify
import shared_variables as var

routes_module = Blueprint('routes_module', __name__)


@routes_module.route('/', methods=["GET"])
def homePage():
    if request.method == 'GET':
        db = var.mongo.db
        users = db.twitusers.find({"verified":0}).sort("user_id").limit(500)
        return render_template('home.html', users=users)


@routes_module.route('/tag/', methods=["POST"])
def tagUser():
    if request.method == 'POST':
        db = var.mongo.db
        user_id = int(request.form["user_id"])
        tag_value = request.form["tag_value"]
        res = db.twitusers.update_one(
            {"user_id": user_id},
            {"$set": {"manual_tag": tag_value}}
        )
        return jsonify({"user_id": user_id, "tag_value": tag_value})
