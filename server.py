#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api

from config import config
from app.controller.consecutive import ConsecutiveTypeController, ConsecutiveController, ConsecutiveActionController
from app.controller.role import RoleController

app = Flask(__name__)

CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

api.add_resource(ConsecutiveTypeController, '/api/admin/consecutive/type')
api.add_resource(ConsecutiveController, '/api/admin/consecutive')

api.add_resource(ConsecutiveActionController, '/api/admin/consecutive/increase/<id>')


api.add_resource(RoleController, '/api/admin/roles')

if __name__ == '__main__':
    app.run(debug=True,port=config.api_port)

