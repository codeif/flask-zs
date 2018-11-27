from flask_sqlalchemy import SQLAlchemy

from flask_zs import BaseModel

db = SQLAlchemy(model_class=BaseModel)
