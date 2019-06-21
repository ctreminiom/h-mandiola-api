#!/usr/bin/env python
# -*- coding: utf-8 -*-

import jwt
import datetime

from config import config
from functools import wraps
from flask import request, jsonify


def createToken(user):

    payload = {
        'user': user,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow(),
    }

    token = jwt.encode(payload, config.jwt_key, algorithm='HS256')

    return token.decode("utf-8")


def decode(token):
    try:
        return jwt.decode(token, config.jwt_key)
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
