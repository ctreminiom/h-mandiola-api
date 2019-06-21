from flask import Blueprint, request, jsonify
from app.utils.jwt import require
from app.modules.consecutiveType.service import ConsecutiveType


consecutive_type_module = Blueprint('consecutive_type_module', __name__)


@consecutive_type_module.route('/api/module/consecutive/type', methods=['POST'])
def create():
    body = request.get_json(silent=True)
    service = ConsecutiveType()

    data = {}
    data["name"] = body["name"]
    data["username"] = "cjt9"

    message = service.create(data)

    resp = jsonify(message["message"])
    resp.status_code = message["status"]

    return resp


@consecutive_type_module.route('/api/module/consecutive/types', methods=['GET'])
#@require
def getAll():
    service = ConsecutiveType()

    data = {}
    data["username"] = "cjt9"

    message = service.getAll(data)

    resp = jsonify(message["message"])
    resp.status_code = message["status"]

    return resp