from db import close_db_conn
from flask import Flask
from flask_cors import CORS


def create_app():

    app = Flask(
        __name__
    )

    CORS(app)
    from .routes import register_app
    app.teardown_appcontext(close_db_conn)
    register_app(app)

    return app