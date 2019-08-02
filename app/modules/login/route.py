from app.modules.login.service import Login
from flask import Blueprint, request, jsonify

import os


login_module = Blueprint('login_module', __name__)


@login_module.route('/api/module/login', methods=['POST'])
def login():
    service = Login()

    body = request.get_json(silent=True)
    data = {}
    data["login_user"] = "admin"

    main_dict = {**body, **data}

    message = service.authenticate(main_dict)

    return jsonify(message["message"]), message["status"]