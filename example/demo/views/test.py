import time

import requests
from flask import Blueprint

from .. import tasks
from ..core import redis_store
from ..exceptions import NoError
from ..forms.test import TestForm

bp = Blueprint("test", __name__, url_prefix="/test")


@bp.route("/form", methods=["POST"])
def form_test():
    form = TestForm()
    form.check()
    raise NoError


@bp.route("/celery")
def celery_test():
    val1 = str(time.time())
    tasks.test.delay(val1)
    time.sleep(0.5)
    val2 = redis_store.get("test:celery")
    print("this is val1, val2", val1, val2)
    assert val1 == val2
    return val1


@bp.route("/baidu")
def baidu():
    return requests.get("https://www.baidu.com")
    # return requests.get('http://httpbin.org/ip')
