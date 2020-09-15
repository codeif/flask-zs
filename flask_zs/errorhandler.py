from flask import jsonify

from .exceptions import CustomException


def register_error_handlers(app):
    @app.errorhandler(CustomException)
    def custom_exception_handler(e):
        return jsonify(errcode=e.errcode, errmsg=e.errmsg, **e.kw)

    @app.errorhandler(401)
    @app.errorhandler(404)
    @app.errorhandler(405)
    def http_exception_handler(e):
        return jsonify(errcode=e.code, errmsg=e.name), e.code
