#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
from flask import Flask
from flask_restful import Resource, Api

from config import config
from app.controller.consecutive import ConsecutiveType

app = Flask(__name__)
api = Api(app)


api.add_resource(ConsecutiveType, '/api/admin/consecutive/type')

if __name__ == '__main__':
    app.run(debug=True,port=config.api_port)
'''


from app.service.consecutive import Consecutive



app = Consecutive()


result = app.create("18", "description", "true", "AAA", "true", "1", "100", "1")


print(result)