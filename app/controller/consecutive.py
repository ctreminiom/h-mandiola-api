#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask import request

from app.service.consecutive import Type, Consecutive

from app.middleware.jwt import require


class ConsecutiveTypeController(Resource):
    @require
    def get(self):
        service = Type()
        message = service.getAll()

        return {'result': message["message"]}, message["status"]

    @require
    def post(self):
        body = request.get_json(silent=True)
        service = Type()

        message = service.create(body["name"])
        return {'result': message["message"]}, message["status"]


class ConsecutiveController(Resource):

    @require
    def post(self):

        body = request.get_json(silent=True)
        service = Consecutive()

        message = service.create(body)
        return {'result': message["message"]}, message["status"]

    @require
    def get(self):
        service = Consecutive()
        message = service.getAll()

        return {'result': message["message"]}, message["status"]


class ConsecutiveActionController(Resource):

    @require
    def put(self, id):
        service = Consecutive()

        message = service.increase(id)

        return {'result': message["message"]}, message["status"]

