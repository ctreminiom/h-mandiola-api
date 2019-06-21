from flask import Blueprint, request, jsonify
from app.utils.jwt import require
from app.modules.error.service import Error

error_module = Blueprint('error_module', __name__)


@error_module.route('/api/module/errors', methods=['GET'])
#@require
def getAll():
    service = Error()

    data = {}
    data["username"] = "cjt9"

    message = service.getAll(data)

    resp = jsonify(message["message"])
    resp.status_code = message["status"]

    return resp