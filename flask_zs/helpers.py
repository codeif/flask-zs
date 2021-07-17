"""
    flask_zs.helpers
    ~~~~~~~~~~~~

    flask-zs helpers module

    :copyright: (c) 2018 by codeif.
    :license: MIT, see LICENSE for more details.
"""

import decimal
import importlib
import json
import uuid
from datetime import date, datetime, time

import requests
from flask import Blueprint, Flask
from werkzeug.utils import find_modules


def register_blueprints(app, import_path, bp_name="bp", include_packages=False, recursive=False):
    """Register all Blueprint instances on the specified Flask application found
    in all modules for the specified package.

    :param app: the Flask application
    :param import_path: the dotted path for the package to find child modules.
    :param bp_name: Blueprint name in views.
    """
    for name in find_modules(import_path, include_packages=include_packages, recursive=recursive):
        mod = importlib.import_module(name)
        bp = getattr(mod, bp_name, None)
        if isinstance(bp, Blueprint):
            app.register_blueprint(bp)


def register_api(bp, view_cls, endpoint, url, pk="item_id", pk_type="int"):
    """register restful api router

    :param bp: flask.BluePrint object
    :param view_cls: flask.views.View class
    :param endpoint: endpint
    :param url: url path, eg: /users/
    :param pk: entity id variable name
    :param pk_type:
        https://flask.palletsprojects.com/en/2.0.x/quickstart/#variable-rules
    """
    view_func = view_cls.as_view(endpoint)
    bp.add_url_rule(url, defaults={pk: None}, view_func=view_func, methods=["GET"])
    bp.add_url_rule(url, view_func=view_func, methods=["POST"])
    bp.add_url_rule(
        "{0}<{1}:{2}>".format(url, pk_type, pk), view_func=view_func, methods=["GET", "PUT", "DELETE", "PATCH"],
    )


class TodictMixin:
    _todict_include = None
    _todict_exclude = None
    _todict_simple = None

    def get_field_names(self):
        # for p in self.__mapper__.iterate_properties:
        #     yield p.key
        # _keys = self.__mapper__.c.keys()
        return [x.name for x in self.__table__.columns]

    def _get_todict_keys(self, include=None, exclude=None, only=None):
        if only:
            return only

        exclude_set = {"password", "created_at"}
        if self._todict_exclude:
            exclude_set.update(self._todict_exclude)
        if exclude:
            exclude_set.update(exclude)

        include_set = set()
        if self._todict_include:
            include_set.update(self._todict_include)
        if include:
            include_set.update(include)

        keys_set = set(self.get_field_names())
        keys_set.difference_update(exclude_set)
        keys_set.update(include_set)

        return keys_set

    def todict(self, include=None, exclude=None, only=None):
        keys = self._get_todict_keys(include, exclude, only)
        data = {key: getattr(self, key) for key in keys}
        return data or None

    def todict_simple(self):
        only = self._todict_simple or [x for x in self._get_todict_keys() if x in ["id", "name"]]
        return self.todict(only=only)


class BaseModel(TodictMixin):
    pass


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        # See "Date Time String Format" in the ECMA-262 specification.
        if isinstance(o, set):
            return list(o)
        if isinstance(o, datetime):
            return o.isoformat(sep=" ", timespec="seconds")
        if isinstance(o, date):
            return o.isoformat()
        if isinstance(o, time):
            return o.isoformat(timespec="minutes")
        if isinstance(o, decimal.Decimal):
            return float(o)
        if isinstance(o, uuid.UUID):
            return str(o)
        if isinstance(o, TodictMixin):
            return o.todict_simple()
        else:
            return super().default(o)


def requests_resp_gen(r):
    while True:
        data = r.raw.read(4096)
        if not data:
            r.close()
            break
        yield data


class CustomFlask(Flask):
    """使用自定义的JSONEncoder，并能处理view直接返回dict"""

    json_encoder = JSONEncoder

    def make_response(self, rv):
        if isinstance(rv, requests.Response):
            headers = rv.headers
            for key in [
                "Server",
                "Connection",
            ]:
                headers.pop(key, None)
            return self.response_class(requests_resp_gen(rv), status=rv.status_code, headers=headers.items(),)

        return super().make_response(rv)


# Views Mixin
class PaginationMixin:
    def item_todict(self, item):
        return item.todict()

    def make_resp(self, query):
        return dict(items=[self.item_todict(x) for x in query])

    def make_pagination_resp(self, query):
        p = query.paginate(error_out=False)
        return dict(
            items=[self.item_todict(x) for x in p.items],
            pagination=dict(total=p.total, page=p.page, per_page=p.per_page, pages=p.pages),
        )
