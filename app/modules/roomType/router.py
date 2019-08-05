from app.modules.roomType.service import RoomType
from flask import Blueprint, request, jsonify
from app.utils.jwt import protected, adminOnly

room_type_module = Blueprint('room_type_module', __name__)

@room_type_module.route('/api/module/room/type', methods=['POST'])
@protected
@adminOnly
def create(data):
    service = RoomType()

    body = request.get_json(silent=True)

    data = {"jwt_user": data['username']}

    main_dict = {**body, **data}

    message = service.create(main_dict)

    return jsonify(message["message"]), message["status"]



@room_type_module.route('/api/module/room/types', methods=['GET'])
@protected
@adminOnly
def getAll(data):
    service = RoomType()

    data = {"jwt_user": data['username']}

    message = service.gets(data)

    return jsonify(message["message"]), message["status"]
