from flask import Blueprint

from flask_zs import BaseItemView, register_api
from ..models.user import User

bp = Blueprint('user', __name__)


class ItemView(BaseItemView):
    item_cls = User


register_api(bp, ItemView, 'item', '/users/')
