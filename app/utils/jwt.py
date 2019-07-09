from config import configuration as conf
from functools import wraps
from flask import request, jsonify

import jwt, datetime



def create(data):

    payload = {
        'username': data["user"],
        'admin': data["admin"],
        'consecutive': data["consecutive"],
        'security': data["security"],
        'queries': data["queries"],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=120),
        'iat': datetime.datetime.utcnow(),
    }

    token = jwt.encode(payload, conf.jwt, algorithm='HS256')

    return token.decode("utf-8")


def check(token):
    try:
        return jwt.decode(token, conf.jwt)
    except jwt.ExpiredSignature:
        return "expired"



def require(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            resp = jsonify("No Access Token")
            resp.status_code = 401

            return resp

        try:
            data = decode(token)

            if data == "expired":
                resp = jsonify("Token Expired")
                resp.status_code = 401

                return resp

            #else:
                 #user = User.objects(public_id=data['public_id']).first()

        except:
            resp = jsonify("Token Invalid")
            resp.status_code = 401

            return resp

        return f("user", *args, **kwargs)

    return decorated