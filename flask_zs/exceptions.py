"""
    flask_zs.exceptions
    ~~~~~~~~~~~~

    Flask-ZS exceptions module

    :copyright: (c) 2018 by codeif.
    :license: MIT, see LICENSE for more details.
"""


class BaseCustomException(Exception):
    errcode = 1000
    errmsg = 'Server Unkown Error.'

    def __init__(self, errmsg=None, errcode=None, **kw):
        if errmsg:
            self.errmsg = errmsg
        if errcode is not None:
            self.errcode = errcode
        self.kw = kw

    def __str__(self):
        return '%d: %s' % (self.errcode, self.errmsg)

    def __repr__(self):
        return '<%s \'%s\'>' % (self.__class__.__name__, self)


class CustomException(BaseCustomException):
    pass


class NoError(CustomException):
    errcode = 0
    errmsg = 'OK'


class FormValidationError(BaseCustomException):
    errcode = 2001
    errmsg = '表单验证错误'

    def __init__(self, form, errmsg=None, show_first_err=True):
        if not errmsg and show_first_err:
            name, errors = next(iter(form.errors.items()))
            errmsg = f'{getattr(form, name).label.text}: {errors[0]}'

        super(FormValidationError, self).__init__(errmsg)
        self.errors = form.errors
