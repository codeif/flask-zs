"""
    flask_zs.exceptions
    ~~~~~~~~~~~~

    flask-zs exceptions module

    :copyright: (c) 2018 by codeif.
    :license: MIT, see LICENSE for more details.
"""


class BaseCustomException(Exception):
    errcode = 1000
    errmsg = "Server Unkown Error."

    def __init__(self, errmsg=None, errcode=None, **kw):
        if errmsg:
            self.errmsg = errmsg
        if errcode is not None:
            self.errcode = errcode
        self.kw = kw

    def __str__(self):
        return "%d: %s" % (self.errcode, self.errmsg)

    def __repr__(self):
        return "<%s '%s'>" % (self.__class__.__name__, self)


class CustomException(BaseCustomException):
    pass


class NoError(CustomException):
    errcode = 0
    errmsg = "OK"
