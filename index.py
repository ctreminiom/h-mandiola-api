from flask import Flask, Blueprint
from flask_restful import Resource, Api

from config import configuration
from app.utils.database import checkOut

application = Flask(__name__)

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


checkOut()

    
if __name__ == "__main__":
    application.run(host="0.0.0.0", port=configuration.port, debug=True)

