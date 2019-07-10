from app.modules.grant.service import Grant
from flask import Blueprint, request, jsonify
from app.utils.jwt import protected, adminOnly


grant_module = Blueprint('grant_module', __name__)

@grant_module.route('/api/module/grant', methods=['POST'])
@protected
@adminOnly
def create(data):
    service = Grant()

    body = request.get_json(silent=True)

    data = {"jwt_user": data['username']}
    main_dict = {**body, **data}

    message = service.create(main_dict)

    return jsonify(message["message"]), message["status"]



@grant_module.route('/api/module/grant', methods=['GET'])
@protected
@adminOnly
def get(data):
    service = Grant()

    args = request.args

    data = {
        "jwt_user": data['username'],
        "username": args['username']
    }

    message = service.get(data)

    return jsonify(message["message"]), message["status"]