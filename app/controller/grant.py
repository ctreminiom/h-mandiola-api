from flask_restful import Resource
from flask import request

from app.service.grant import Grant
from app.middleware.jwt import require


class CreateGrant(Resource):
    def post(self):

        body = request.get_json(silent=True)
        service = Grant()

        message = service.create(body)
        return {'result': message["message"]}, message["status"]


class GetGrants(Resource):
    def get(self):
        service = Grant()
        message = service.getAll()

        return {'result': message["message"]}, message["status"]



class RemoveGrant(Resource):
    def delete(self, body):
        body = request.get_json(silent=True)
        service = Grant()

        message = service.remove(body)
        return {'result': message["message"]}, message["status"]


