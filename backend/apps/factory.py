from flask import Flask
from flask_cors import CORS

from apps.user.web import user_api_v1
from apps.cep.web import cep_api_v1


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(user_api_v1)
    app.register_blueprint(cep_api_v1)

    return app
