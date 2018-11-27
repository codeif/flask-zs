from flask import Blueprint

from flask_zs.exceptions import NoError

bp = Blueprint('general', __name__)


@bp.route('/')
def index():
    return 'hello2'
    # raise NoError


@bp.route('/ok')
def no_error():
    raise NoError
