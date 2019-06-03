from flask_restful import Resource
from flask import request

from app.service.activity import Activity
from app.middleware.jwt import require



class CreateActivity(Resource):
    def post(self):

        body = {
            "consecutive" : request.form['consecutive'],
            "name" : request.form['name'],
            "description" : request.form['description'],
            "image_path": request.files['image']
        }

        print(body)

        service = Activity()

        message = service.create(body)
        return {'result': message["message"]}, message["status"]




class GetActivities(Resource):
    def get(self):
        service = Activity()
        message = service.getAll()

        return {'result': message["message"]}, message["status"]


class RemoveActivity(Resource):
    def delete(self, id):
        service = Activity()
        message = service.remove(id)

        return {'result': message["message"]}, message["status"]


class UpdateActivity(Resource):
    def put(self, id):
        service = Activity()
        body = request.get_json(silent=True)

        print(body)


        message = service.update(body, id)

        return {'result': message["message"]}, message["status"]


class UpdateActivityImage(Resource):
    def put(self, id):
        body = {"image_path": request.files['image']}
        service = Activity()

        message = service.updateImage(body, id)

        return {'result': message["message"]}, message["status"]
