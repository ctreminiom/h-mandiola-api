from flask_restful import Resource
from flask import request

from app.service.activity import Activity
from app.middleware.jwt import require



class CreateActivity(Resource):
    
    def post(self):
        body = request.get_json(silent=True)
        service = Activity()

        message = service.create(body)
        return {'result': message["message"]}, message["status"]




class GetActivities(Resource):
    def get(self):
        service = Activity()
        message = service.getAll()

        return {'result': message["message"]}, message["status"]