from flask_restful import Resource
from flask import request

from app.service.role import Role
from app.middleware.jwt import require


class CreateRole(Resource):
    def post(self):

        body = request.get_json(silent=True)
        service = Role()

        message = service.create(body["name"])
        return {'result': message["message"]}, message["status"]


class GetRoles(Resource):
    def get(self):
        service = Role()
        message = service.getAll()

        return {'result': message["message"]}, message["status"]

