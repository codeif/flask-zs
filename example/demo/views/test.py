from flask import Blueprint

from ..exceptions import NoError
from ..forms.test import TestForm

bp = Blueprint('test', __name__, url_prefix='/test')


@bp.route('/form', methods=['POST'])
def form_test():
    form = TestForm()
    form.check()
    raise NoError
