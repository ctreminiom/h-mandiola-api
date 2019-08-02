from app.modules.consecutive.service import Consecutive
from flask import Blueprint, request, jsonify
from app.utils.jwt import protected, adminOnly

consecutive_module = Blueprint('consecutive_module', __name__)

@consecutive_module.route('/api/module/consecutive', methods=['POST'])
@protected
@adminOnly
def create(data):
    service = Consecutive()

    body = request.get_json(silent=True)

    data = {"jwt_user": data['username']}
    main_dict = {**body, **data}

    message = service.create(main_dict)

    return jsonify(message["message"]), message["status"]


@consecutive_module.route('/api/module/consecutives', methods=['GET'])
@protected
@adminOnly
def getAll(data):
    service = Consecutive()

    data = {"jwt_user": data['username']}

    message = service.gets(data)

    return jsonify(message["message"]), message["status"]