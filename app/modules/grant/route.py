from app.modules.grant.service import Grant
from flask import Blueprint, request, jsonify


grant_module = Blueprint('grant_module', __name__)

@grant_module.route('/api/module/grant', methods=['POST'])
def create():
    service = Grant()

    body = request.get_json(silent=True)

    data = {}
    data["jwt_user"] = "cjt9"

    main_dict = {**body, **data}

    print(main_dict)

    message = service.create(main_dict)

    print(message)

    resp = jsonify(message["message"])
    resp.status_code = message["status"]

    return resp



@grant_module.route('/api/module/grant', methods=['GET'])
def get():
    service = Grant()

    args = request.args

    data = {}
    data["jwt_user"] = "cjt9"
    data["username"] = args['username']

    message = service.get(data)

    resp = jsonify(message["message"])
    resp.status_code = message["status"]

    return resp