from flask import request
from pydantic import BaseModel


class BaseJsonModel(BaseModel):
    def __init__(self):
        data = request.get_json()
        super().__init__(**data)


class BaseQueryModel(BaseModel):
    def __init__(self):
        data = request.args
        super().__init__(**data)
