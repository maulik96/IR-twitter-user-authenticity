from flask import Blueprint, request, render_template, jsonify
import shared_variables as var

routes_module = Blueprint('routes_module', __name__)


@routes_module.route('/', methods=["GET"])
def homePage():
    if request.method == 'GET':
        db = var.mongo.db
        res = db.twitusers.find().sort("authenticity_score")
        return render_template('home.html', users=res)


@routes_module.route('/tag/<user_id>/<tag_value>', methods=["POST"])
def tagUser():
    if request.method == 'POST':
        db = var.mongo.db
        res = db.twitusers.update_one(
            {"user_id": user_id},
            {"$set": {"manual_tag": tag_value}},
            upsert=False
        )
        return jsonify(res)
