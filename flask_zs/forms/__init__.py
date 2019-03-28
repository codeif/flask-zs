from flask import request
from wtforms import Form

from ..exceptions import FormValidationError

__all__ = (
    'BaseItemForm',
    'BaseQueryForm',
    'Form',
    'JSONForm',
)


class JSONForm(Form):
    class Meta:
        locales = ['zh']

    def __init__(self):
        data = request.get_json()
        super().__init__(data=data)

    def check(self):
        if not self.validate():
            raise FormValidationError(self)


class BaseItemForm(JSONForm):
    def __init__(self, item):
        self.item = item
        super().__init__()


class BaseQueryForm(Form):
    def __init__(self):
        super().__init__(formdata=request.args)
