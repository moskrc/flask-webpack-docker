import os

from flask import Flask

from .core import bp as core_bp
from config import config as project_config
from flask_webpack_loader import WebpackLoader

basedir = os.path.abspath(os.path.dirname(__file__))


def create_app(config_name: str):
    print(config_name)
    app = Flask(__name__, static_folder='static')

    if not isinstance(config_name, str):
        config_name = os.getenv('FLASK_CONFIG', 'default')

    app.config.from_object(project_config[config_name])

    project_config[config_name].init_app(app)

    app.register_blueprint(core_bp, url_prefix=None)

    webpack_loader = WebpackLoader(app)

    return app
