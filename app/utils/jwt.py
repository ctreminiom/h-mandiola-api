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
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=500),
        'iat': datetime.datetime.utcnow(),
    }

    token = jwt.encode(payload, conf.jwt, algorithm='HS256')

    return token.decode("utf-8")


def check(token):
    try:
        return jwt.decode(token, conf.jwt)
    except jwt.ExpiredSignature as err:
        return str(err)

def protected(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
            token_cleared = token.replace('Bearer ', '')
            token = token_cleared

        if not token:
            return jsonify({'message': "no access token"}), 403

        try:
            data = check(token)
            if data == "expired": return jsonify({'message': "token expired"}), 403
        except:
            return jsonify({'message': "token Invalid"}), 403

        return f(data, *args, **kwargs)

    return decorated


def adminOnly(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
            token_cleared = token.replace('Bearer ', '')
            token = token_cleared

        if not token:
            return jsonify({'message': "no access token"}), 403

        try:
            data = check(token)
            if data == "expired": return jsonify({'message': "token expired"}), 403

            if  data['admin']:
                return f(*args, **kwargs)
            else:
                return jsonify({'message': 'unauthorized'}), 401

        except Exception as err:
            print(err)
            return jsonify({'message': str(err)}), 403

        return f(*args, **kwargs)

    return decorated


def securityOnly(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
            token_cleared = token.replace('Bearer ', '')
            token = token_cleared

        if not token:
            return jsonify({'message': "no access token"}), 403

        try:
            data = check(token)
            if data == "expired": return jsonify({'message': "token expired"}), 403

            if data['security'] or data['admin']:
                return f(*args, **kwargs)
            else:
                return jsonify({'message': 'unauthorized'}), 401

        except Exception as err:
            print(err)
            return jsonify({'message': "token Invalid"}), 403

        return f(*args, **kwargs)

    return decorated


def consecutiveOnly(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
            token_cleared = token.replace('Bearer ', '')
            token = token_cleared

        if not token:
            return jsonify({'message': "no access token"}), 403

        try:
            data = check(token)
            if data == "expired": return jsonify({'message': "token expired"}), 403

            if data['consecutive'] or data['admin']:
                return f(*args, **kwargs)
            else:
                return jsonify({'message': 'unauthorized'}), 401

        except:
            return jsonify({'message': "token Invalid"}), 403

        return f(*args, **kwargs)

    return decorated


def queryOnly(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
            token_cleared = token.replace('Bearer ', '')
            token = token_cleared

        if not token:
            return jsonify({'message': "no access token"}), 403

        try:
            data = check(token)
            if data == "expired": return jsonify({'message': "token expired"}), 403

            print(data['queries'])

            if data['queries'] == True or data['admin'] == True:
                print("asss")
            else:
                return jsonify({'message': 'unauthorized'}), 401

        except:
            return jsonify({'message': "token Invalid"}), 403

        return f(*args, **kwargs)

    return decorated
