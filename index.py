from flask import Flask, Blueprint
from flask_restful import Resource, Api

from config import configuration
from app.utils.database import checkOut

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"



from app.modules.role.route import role_module
app.register_blueprint(role_module)


from app.modules.log.route import log_module
app.register_blueprint(log_module)


from app.modules.error.route import error_module
app.register_blueprint(error_module)


from app.modules.user.route import user_module
app.register_blueprint(user_module)

from app.modules.login.route import login_module
app.register_blueprint(login_module)


checkOut()

    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=configuration.port, debug=True)

