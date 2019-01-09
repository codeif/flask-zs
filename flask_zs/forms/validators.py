import re

from wtforms.validators import (
    URL, UUID, AnyOf, DataRequired, Email, EqualTo, InputRequired, IPAddress, Length, MacAddress, NoneOf, NumberRange)
from wtforms.validators import Optional as Optional_
from wtforms.validators import (
    Regexp, StopValidation, ValidationError, any_of, data_required, email, equal_to, input_required, ip_address, length,
    mac_address, none_of, number_range, regexp, url)

__all__ = (
    'DataRequired', 'data_required', 'Email', 'email', 'EqualTo', 'equal_to',
    'IPAddress', 'ip_address', 'InputRequired', 'input_required', 'Length',
    'length', 'NumberRange', 'number_range', 'Optional',
    'Regexp', 'regexp', 'URL', 'url', 'AnyOf',
    'any_of', 'NoneOf', 'none_of', 'MacAddress', 'mac_address', 'UUID',
    'ValidationError', 'StopValidation', 'PhoneNumber', 'Range'
)

PHONE_REGEX = r'^1[3-9]\d{9}$'
PHONE_PATERN = re.compile(PHONE_REGEX)


class PhoneNumber(Regexp):
    def __init__(self):
        super().__init__(PHONE_PATERN, message='手机号格式错误')


class Optional(Optional_):
    def __call__(self, form, field):
        if field.data is None or isinstance(field.data, str) and not self.string_check(field.data):
            field.errors[:] = []
            raise StopValidation


class Range(object):
    def __init__(self, min=None, max=None, message=None):
        self.min = min
        self.max = max
        self.message = message

    def __call__(self, form, field):
        data = field.data
        if data is None or (self.min is not None and data < self.min) or \
                (self.max is not None and data > self.max):
            message = self.message
            if message is None:
                # we use %(min)s interpolation to support floats, None, and
                # Decimals without throwing a formatting exception.
                if self.max is None:
                    message = field.gettext('不能小于 %(min)s.')
                elif self.min is None:
                    message = field.gettext('不能大于 %(max)s.')
                else:
                    message = field.gettext('必须在 %(min)s 和 %(max)s之间.')

            raise ValidationError(message % dict(min=self.min, max=self.max))
