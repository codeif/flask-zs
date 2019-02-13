from flask import Blueprint

from flask_zs import BaseItemView, register_api
from ..forms.user import UserForm
from ..models.user import User

bp = Blueprint('user', __name__)


class ItemView(BaseItemView):
    item_cls = User
    item_form_cls = UserForm


register_api(bp, ItemView, 'item', '/users/')
