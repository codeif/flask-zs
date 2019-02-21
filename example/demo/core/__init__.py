from celery import Celery
from flask import current_app
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy
from flask_zs import BaseModel
from werkzeug.local import LocalProxy

logger = LocalProxy(lambda: current_app.logger)
db = SQLAlchemy(model_class=BaseModel)
redis_store = FlaskRedis(decode_responses=True, decode_components=True)
celery = Celery(include=['demo.tasks'])
