from app.modules.log.service import Log
from flask import Blueprint, request, jsonify


log_module = Blueprint('log_module', __name__)


@log_module.route('/api/module/logs', methods=['GET'])
# @require
def getAll():
    service = Log()

    data = {}
    data["username"] = "cjt9"

    message = service.getAll(data)

    resp = jsonify(message["message"])
    resp.status_code = message["status"]

    return resp
