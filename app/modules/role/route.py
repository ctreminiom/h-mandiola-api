from app.modules.role.service import Role
from flask import Blueprint, request, jsonify
from app.utils.jwt import protected, adminOnly

role_module = Blueprint('role_module', __name__)

@role_module.route('/api/module/role', methods=['POST'])
@protected
@adminOnly
def create(data):
    service = Role()

    body = request.get_json(silent=True)

    data = {"jwt_user": data['username']}

    main_dict = {**body, **data}

    message = service.create(main_dict)

    return jsonify(message["message"]), message["status"]



@role_module.route('/api/module/roles', methods=['GET'])
@protected
@adminOnly
def getAll(data):
    service = Role()

    data = {"jwt_user": data['username']}

    message = service.gets(data)

    return jsonify(message["message"]), message["status"]
