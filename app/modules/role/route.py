from app.modules.role.service import Role
from flask import Blueprint, request, jsonify


role_module = Blueprint('role_module', __name__)

@role_module.route('/api/module/role', methods=['POST'])
def create():
    service = Role()

    body = request.get_json(silent=True)

    data = {}
    data["username"] = "cjt9"

    main_dict = {**body, **data}

    print(main_dict)

    message = service.create(main_dict)

    resp = jsonify(message["message"])
    resp.status_code = message["status"]

    return resp



@role_module.route('/api/module/roles', methods=['GET'])
def getAll():
    service = Role()

    data = {}
    data["username"] = "cjt9"

    message = service.getAll(data)

    resp = jsonify(message["message"])
    resp.status_code = message["status"]

    return resp
