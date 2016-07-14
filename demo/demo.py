# demo.py
# demo file for Demo App
# author = JP Villavicencio
# email = jefferson.villavicencio@team.telstra.com
# status = Prototype
# last revision = 11 July 2016

from bson import json_util
from flask import Response


def to_json(data):
    return json_util.dumps(data, default=json_util.default)


def json_resp(json_doc):
    resp = Response(json_doc)
    resp.headers['Content-Type'] = 'application/json'
    return resp
