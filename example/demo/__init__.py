from flask_zs import CustomFlask, register_blueprints
from .core import commands, db


def create_app():
    app = CustomFlask(__name__)
    app.config.from_object('demo.config.Config')
    db.init_app(app)

    register_blueprints(app, 'demo.views')

    print('hahaha')
    commands.init_app(app)

    return app
