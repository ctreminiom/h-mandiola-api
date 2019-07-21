from flask import Flask, Blueprint
from flask_restful import Resource, Api

from config import configuration
from app.utils.database import checkOut

from flask_cors import CORS

import os

application = Flask(__name__)
CORS(application)

@application.route("/")
def hello():
    return "Hello World!"



from app.modules.role.route import role_module
application.register_blueprint(role_module)


from app.modules.log.route import log_module
application.register_blueprint(log_module)


from app.modules.error.route import error_module
application.register_blueprint(error_module)


from app.modules.user.route import user_module
application.register_blueprint(user_module)

from app.modules.login.route import login_module
application.register_blueprint(login_module)


from app.modules.grant.route import grant_module
application.register_blueprint(grant_module)

from app.modules.consecutiveType.router import type_module
application.register_blueprint(type_module)


from app.modules.consecutive.router import consecutive_module
application.register_blueprint(consecutive_module)

from app.modules.activity.router import activity_module
application.register_blueprint(activity_module)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
GOOGLE_CLOUD = ROOT_DIR + "/docs/h-mandiola-beb59920ed9d.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_CLOUD

ASSETS = ROOT_DIR + "/assets/"
os.environ["ASSETS_PATH"] = ASSETS


    
if __name__ == "__main__":
    application.run(host="0.0.0.0", port=configuration.port, debug=True)

