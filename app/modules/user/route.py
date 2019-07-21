from app.modules.user.service import User
from flask import Blueprint, request, jsonify
from app.utils.jwt import protected, securityOnly



user_module = Blueprint('user_module', __name__)


@user_module.route('/api/module/user', methods=['POST'])
@protected
@securityOnly
def create(data):
    service = User()

    body = request.get_json(silent=True)

    data = {"jwt_user": data['username']}


    main_dict = {**body, **data}

    message = service.create(main_dict)

    return jsonify(message["message"]), message["status"]


@user_module.route('/api/module/users', methods=['GET'])
@protected
@securityOnly
def getAll(data):
    service = User()

    data = {"jwt_user": data['username']}

    message = service.gets(data)

    return jsonify(message["message"]), message["status"]



@user_module.route('/api/module/user', methods=['GET'])
@protected
@securityOnly
def getByUsername(data):
    service = User()

    args = request.args

    data = {"jwt_user": data['username'], 'username': args['username']}

    message = service.get(data)

    return jsonify(message["message"]), message["status"]


@user_module.route('/api/module/user', methods=['PUT'])
@protected
@securityOnly
def updatePass(data):
    service = User()

    args = request.args
    data = {"jwt_user": data['username'], 'username': args['username']}

    body = request.get_json(silent=True)

    main_dict = {**body, **data}

    message = service.updatePassword(main_dict)

    return jsonify(message["message"]), message["status"]

