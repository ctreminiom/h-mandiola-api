from app.modules.activity.service import Activity
from flask import Blueprint, request, jsonify
from app.utils.jwt import protected, adminOnly

activity_module = Blueprint('activity_module', __name__)

@activity_module.route('/api/module/activity', methods=['POST'])
@protected
@adminOnly
def create(data):
    service = Activity()

    body = {
            "consecutive" : request.form['consecutive'],
            "name" : request.form['name'],
            "description" : request.form['description'],
            "image_path": request.files['image']
        }


    data = {"jwt_user": data['username']}
    main_dict = {**body, **data}

    message = service.create(main_dict)

    return jsonify(message["message"]), message["status"]


@activity_module.route('/api/module/activities', methods=['GET'])
@protected
@adminOnly
def getAll(data):
    service = Activity()

    data = {"jwt_user": data['username']}

    message = service.gets(data)

    return jsonify(message["message"]), message["status"]