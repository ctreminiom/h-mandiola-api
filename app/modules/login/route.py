from app.modules.login.service import Login
from flask import Blueprint, request, jsonify


login_module = Blueprint('login_module', __name__)


@login_module.route('/api/module/login/signIn', methods=['POST'])
def login():
    service = Login()

    body = request.get_json(silent=True)
    data = {}
    data["login_user"] = "admin"

    main_dict = {**body, **data}

    message = service.authenticate(main_dict)

    resp = jsonify(message["message"])
    resp.status_code = message["status"]

    return resp