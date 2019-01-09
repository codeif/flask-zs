from datetime import datetime

from wtforms import DateField as DateField_
from wtforms import DateTimeField as DateTimeField_
from wtforms import DecimalField, Field, FloatField
from wtforms import IntegerField as IntegerField_
from wtforms import PasswordField
from wtforms import SelectField as SelectField_
from wtforms import SelectMultipleField

__all__ = (
    'BooleanField',
    'DateField',
    'DateTimeField',
    'DecimalField',
    'Field',
    'FloatField',
    'IntegerField',
    'ListField',
    'PasswordField',
    'SelectField',
    'SelectMultipleField',
    'StringField',
)


class StringField(Field):
    def process_data(self, value):
        if value is None:
            self.data = value
            return
        if not isinstance(value, str):
            self.data = None
            raise ValueError('不是字符串')
        self.data = value


class IntegerField(IntegerField_):
    def process_data(self, value):
        if value is None:
            self.data = None
            return
        try:
            self.data = int(value)
        except (ValueError, TypeError):
            self.data = None
            raise ValueError(self.gettext('Not a valid integer value'))


class BooleanField(Field):
    def process_data(self, value):
        self.data = bool(value)


class StrictBooleanField(Field):
    def process_data(self, value):
        self.data = value
        if not isinstance(value, bool):
            raise ValueError('不是有效的bool类型')


class SelectField(SelectField_):
    def process_data(self, value):
        if value is None:
            self.data = value
        else:
            super().process_data(value)


class DateTimeField(DateTimeField_):
    def process_data(self, value):
        if not value:
            self.data = None
            return
        try:
            self.data = datetime.strptime(value, self.format)
        except ValueError:
            self.data = None
            raise ValueError(self.gettext('Not a valid datetime value'))


class DateField(DateField_):
    def process_data(self, value):
        if not value:
            self.data = None
            return
        try:
            self.data = datetime.strptime(value, self.format).date()
        except ValueError:
            self.data = None
            raise ValueError(self.gettext('Not a valid date value'))


class ListField(Field):
    def process_data(self, value):
        if not (value is None or isinstance(value, list)):
            self.data = None
            raise ValueError('不是有效的列表')
        self.data = value
