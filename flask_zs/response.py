from flask import jsonify


def make_msg(code, msg):
    return jsonify(errcode=code, errmsg=msg)
