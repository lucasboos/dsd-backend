import os
import configparser

from apps.factory import create_app
from apps.sql_alchemy import db


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read(os.path.abspath(os.path.join(".ini")))

    app = create_app()
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://<user>:<password>@<server>:<port>/<database>'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["JWT_SECRET_KEY"] = '3Qv7SEEvX3TbkcNf'

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.run(port=5001)
