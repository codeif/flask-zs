from flask import jsonify


def ok_resp():
    return jsonify(errcode=0, errmsg='ok')
