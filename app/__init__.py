from flask import Flask
import sqlite3

from app.views import views
from app.auth import auth

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "this is a secret key, don't share"

    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')

    return app
