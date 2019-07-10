from app.modules.log.service import Log
from flask import Blueprint, request, jsonify

from app.utils.jwt import protected, queryOnly


log_module = Blueprint('log_module', __name__)

@log_module.route('/api/module/logs', methods=['GET'])
@protected
@queryOnly
def getAll(data):
    service = Log()

    data = {"jwt_user": data['username']}

    message = service.getAll(data)

    return jsonify(message["message"]), message["status"]
