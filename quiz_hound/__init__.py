from config import Config
from flask import Flask
from quiz_hound.views import auth, index


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(index.bp)
    app.register_blueprint(auth.bp)
    return app
