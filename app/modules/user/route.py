from app.modules.user.service import User
from flask import Blueprint, request, jsonify


user_module = Blueprint('user_module', __name__)


@user_module.route('/api/module/user', methods=['POST'])
def create():
    service = User()

    body = request.get_json(silent=True)

    data = {}
    data["jwt_user"] = "cjt9"

    main_dict = {**body, **data}

    message = service.create(main_dict)

    resp = jsonify(message["message"])
    resp.status_code = message["status"]

    return resp


@user_module.route('/api/module/users', methods=['GET'])
def getAll():
    service = User()

    data = {}
    data["jwt_user"] = "cjt9"

    message = service.getAll(data)

    resp = jsonify(message["message"])
    resp.status_code = message["status"]

    return resp



@user_module.route('/api/module/user', methods=['GET'])
def getByUsername():
    service = User()

    args = request.args

    data = {}
    data["jwt_user"] = "cjt9"
    data["username"] = args['username']

    message = service.getByUsername(data)

    resp = jsonify(message["message"])
    resp.status_code = message["status"]

    return resp

