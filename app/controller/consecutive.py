#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask import request

from app.service.consecutive import Type

class ConsecutiveType(Resource):

    def get(self):
        handler = Type()
        types = handler.gets()

        return {'result': types}, 200


    def post(self):
        data = request.get_json(silent=True)

        handler = Type()

        response = handler.create(data["name"])

        return {'result': response}, 201

    
        


        
