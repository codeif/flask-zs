from flask_zs import CustomFlask, register_blueprints, register_error_handlers

from .core import celery, commands, db, redis_store


def create_app():
    app = CustomFlask(__name__, instance_relative_config=True)
    app.config.from_object('demo.default_settings')
    app.config.from_pyfile('application.cfg', silent=True)
    db.init_app(app)

    register_blueprints(app, 'demo.views')

    redis_store.init_app(app)
    commands.init_app(app)
    init_celery(app, celery)

    register_error_handlers(app)

    return app


def init_celery(app, celery):
    celery.main = app.import_name
    celery.conf.update(
        broker_url=app.config['CELERY_BROKER_URL'],
        result_backend=app.config.get('CELERY_RESULT_BACKEND'),
    )

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery
