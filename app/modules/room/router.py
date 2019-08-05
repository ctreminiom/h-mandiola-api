from app.modules.room.service import Room
from flask import Blueprint, request, jsonify
from app.utils.jwt import protected, adminOnly

room_module = Blueprint('room_module', __name__)

@room_module.route('/api/module/room', methods=['POST'])
@protected
@adminOnly
def create(data):
    service = Room()

    body = {
            "consecutive" : request.form['consecutive'],
            "room_type_ID" : request.form['room_type_ID'],
            "number" : request.form['number'],
            "description": request.form['description'],
            "available": request.form['available'],
            "image_path": request.files['image_path']
        }


    data = {"jwt_user": data['username']}

    main_dict = {**body, **data}

    message = service.create(main_dict)

    return jsonify(message["message"]), message["status"]



@room_module.route('/api/module/rooms', methods=['GET'])
@protected
@adminOnly
def getAll(data):
    service = Room()

    data = {"jwt_user": data['username']}

    message = service.gets(data)

    return jsonify(message["message"]), message["status"]
