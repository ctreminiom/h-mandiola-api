#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask import request

from app.service.consecutive import Type, Consecutive

from app.utils.jwt import require


class CreateConsecutiveType(Resource):
    def post(self):
        body = request.get_json(silent=True)
        service = Type()

        message = service.create(body["name"])
        return {'result': message["message"]}, message["status"]


class GetConsecutivesTypes(Resource):
    def get(self):
        service = Type()
        message = service.getAll()

        return {'result': message["message"]}, message["status"]


class CreateConsecutive(Resource):
    def post(self):

        body = request.get_json(silent=True)
        service = Consecutive()

        message = service.create(body)
        return {'result': message["message"]}, message["status"]


class GetConsecutives(Resource):
    def get(self):
        service = Consecutive()
        message = service.getAll()

        return {'result': message["message"]}, message["status"]


class IncreaseConsecutive(Resource):
    def put(self, id):
        service = Consecutive()

        message = service.increase(id)

        return {'result': message["message"]}, message["status"]


class UpdateConsecutive(Resource):
    def put(self, id):

        body = request.get_json(silent=True)
        service = Consecutive()

        message = service.update(id, body)

        return {'result': message["message"]}, message["status"]
        


class ConsecutiveController(Resource):

    def post(self):

        body = request.get_json(silent=True)
        service = Consecutive()

        message = service.create(body)
        return {'result': message["message"]}, message["status"]

    def get(self):
        service = Consecutive()
        message = service.getAll()

        return {'result': message["message"]}, message["status"]


class ConsecutiveActionController(Resource):

    def put(self, id):
        service = Consecutive()

        message = service.increase(id)

        return {'result': message["message"]}, message["status"]

