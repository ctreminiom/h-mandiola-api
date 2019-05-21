#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Resource, Api

from config import config
from app.controller.consecutive import ConsecutiveTypeController, ConsecutiveController, ConsecutiveActionController

app = Flask(__name__)
api = Api(app)


api.add_resource(ConsecutiveTypeController, '/api/admin/consecutive/type')
api.add_resource(ConsecutiveController, '/api/admin/consecutive')

api.add_resource(ConsecutiveActionController, '/api/admin/consecutive/increase/<id>')

if __name__ == '__main__':
    app.run(debug=True,port=config.api_port)

