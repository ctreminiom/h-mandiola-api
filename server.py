#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api

from config import config

from app.controller.consecutive import ConsecutiveTypeController, ConsecutiveController, ConsecutiveActionController
from app.controller.role import CreateRole, GetRoles


from app.controller.user import CreateUser, GetAllUsers, GetUserByUsername, ChangeUserPassword, Login

from app.controller.grant import CreateGrant, GetGrants, RemoveGrant

app = Flask(__name__)

CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

api.add_resource(ConsecutiveTypeController, '/api/admin/consecutive/type')

api.add_resource(ConsecutiveController, '/api/admin/consecutive')
api.add_resource(ConsecutiveActionController, '/api/admin/consecutive/increase/<id>')


api.add_resource(CreateUser, '/api/admin/user')
api.add_resource(GetAllUsers, '/api/admin/users')
api.add_resource(GetUserByUsername, '/api/admin/user')
api.add_resource(ChangeUserPassword, '/api/admin/user/change/password')
api.add_resource(Login, '/api/admin/login')


api.add_resource(CreateRole, '/api/admin/role')
api.add_resource(GetRoles, '/api/admin/roles')


api.add_resource(CreateGrant, '/api/admin/grant')
api.add_resource(GetGrants, '/api/admin/grants')
api.add_resource(RemoveGrant, '/api/admin/remove/grant')



if __name__ == '__main__':
    app.run(debug=True,port=config.api_port)

