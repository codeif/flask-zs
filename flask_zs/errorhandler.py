from flask import jsonify

from .exceptions import CustomException, FormValidationError


def register_error_handlers(app):
    @app.errorhandler(CustomException)
    def custom_exception_handler(e):
        return jsonify(errcode=e.errcode, errmsg=e.errmsg, **e.kw)

    @app.errorhandler(FormValidationError)
    def form_validation_err_handler(e):
        return jsonify(errcode=e.errcode, errmsg=e.errmsg, errors=e.errors, **e.kw)

    @app.errorhandler(404)
    @app.errorhandler(405)
    def http_exception_handler(e):
        return jsonify(errcode=e.code, errmsg=e.name), e.code

    @app.errorhandler(401)
    def http_401_handler(e):
        # resp = jsonify(errcode=e.code, errmsg=e.name)
        resp = e.get_response()
        # resp.headers['WWW-Authenticate'] = 'Basic realm="Restricted Content"'
        resp.headers['WWW-Authenticate'] = 'Basic realm="Private Property"'
        return resp
