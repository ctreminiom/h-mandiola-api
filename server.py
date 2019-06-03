#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api

from config import config

from app.controller.consecutive import CreateConsecutiveType, GetConsecutivesTypes
from app.controller.consecutive import CreateConsecutive, GetConsecutives, IncreaseConsecutive, UpdateConsecutive
from app.controller.role import CreateRole, GetRoles
from app.controller.user import CreateUser, GetAllUsers, GetUserByUsername, ChangeUserPassword, Login
from app.controller.grant import CreateGrant, GetGrants, RemoveGrant
from app.controller.activity import CreateActivity, GetActivities, RemoveActivity, UpdateActivity, UpdateActivityImage

app = Flask(__name__)

CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

api.add_resource(CreateConsecutiveType, '/api/admin/consecutive/type')
api.add_resource(GetConsecutivesTypes, '/api/admin/consecutive/types')

api.add_resource(CreateConsecutive, '/api/admin/consecutive')
api.add_resource(GetConsecutives, '/api/admin/consecutives')
api.add_resource(UpdateConsecutive, '/api/admin/consecutive/<id>')
api.add_resource(IncreaseConsecutive, '/api/admin/consecutive/increase/<id>')

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

api.add_resource(CreateActivity, '/api/admin/activity')
api.add_resource(GetActivities, '/api/admin/activities')
api.add_resource(RemoveActivity, '/api/admin/activity/<id>')
api.add_resource(UpdateActivity, '/api/admin/activity/<id>')
api.add_resource(UpdateActivityImage, '/api/admin/activity/image/<id>')


if __name__ == '__main__':
    app.run(debug=True,port=config.api_port)

