from app.modules.consecutiveType.service import Type
from app.modules.role.service import Role
from flask import Blueprint, request, jsonify
from app.utils.jwt import protected, adminOnly

type_module = Blueprint('type_module', __name__)

@type_module.route('/api/module/consecutive/type', methods=['POST'])
@protected
@adminOnly
def create(data):
    service = Type()

    body = request.get_json(silent=True)

    data = {"jwt_user": data['username']}
    main_dict = {**body, **data}

    message = service.create(main_dict)

    return jsonify(message["message"]), message["status"]


@type_module.route('/api/module/consecutive/types', methods=['GET'])
@protected
@adminOnly
def getAll(data):
    service = Type()

    data = {"jwt_user": data['username']}

    message = service.gets(data)

    return jsonify(message["message"]), message["status"]