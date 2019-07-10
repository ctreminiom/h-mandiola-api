from app.modules.error.service import Error
from flask import Blueprint, request, jsonify
from app.utils.jwt import protected, queryOnly



error_module = Blueprint('error_module', __name__)


@error_module.route('/api/module/errors', methods=['GET'])
@protected
@queryOnly
def getAll(data):
    service = Error()

    data = {"jwt_user": data['username']}
    message = service.getAll(data)

    return jsonify(message["message"]), message["status"]
