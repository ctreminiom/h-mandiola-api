#!/usr/bin/env python
# -*- coding: utf-8 -*-

import jwt
import datetime

from config import config
from functools import wraps
from flask import request


def encode(user):

    payload = {
        'public_id': user.username,
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
            return {"message": "No Access Token"}, 401

        try:
            data = decode(token)

            if data == "expired":
                return {"message": "Token Expired"}, 401
            #else:
                 #user = User.objects(public_id=data['public_id']).first()

        except:
            return {"message": "Token Invalid"}, 401

        return f("user", *args, **kwargs)

    return decorated
