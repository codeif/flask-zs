from flask import jsonify


def make_json_errmsg(errcode=0, errmsg="success", **kwargs):
    return jsonify(errcode=errcode, errmsg=errmsg, **kwargs)
