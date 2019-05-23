from flask_restful import Resource
from flask import request

from app.service.user import User
from app.middleware.jwt import require



class ChangeUserPassword(Resource):
    def put(self):

        body = request.get_json(silent=True)
        service = User()

        print(body)

        message = service.changePassword(body)
        return {'result': message["message"]}, message["status"]

class GetUserByUsername(Resource):
    def get(self):

        args = request.args
        print (args) # For debugging

        username = args['username']

        service = User()
        message = service.getByUsername(username)

        return {'result': message["message"]}, message["status"]

class GetAllUsers(Resource):
    def get(self):
        service = User()
        message = service.getAll()

        return {'result': message["message"]}, message["status"]


class CreateUser(Resource):
    def post(self):
        body = request.get_json(silent=True)
        service = User()

        message = service.create(body)
        return {'result': message["message"]}, message["status"]



class Login(Resource):
    def post(self):
        body = request.get_json(silent=True)
        service = User()

        message = service.login(body)
        return {'result': message["message"]}, message["status"]
