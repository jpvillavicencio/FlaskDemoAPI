# blueprint/postcode.py
# Main file for Demo App
# author = JP Villavicencio
# email = jefferson.villavicencio@team.telstra.com
# status = Prototype
# last revision = 15 July 2016

from flask import Blueprint, abort, request, make_response, jsonify
from .doc import auto
from .demo import to_json, json_resp
import mongo


postcode_blueprint = Blueprint('postcode', __name__, url_prefix='/api/postcode')
db = mongo.mongo_test


@postcode_blueprint.route('/', methods=['GET'])
@auto.doc(groups=['postcode', 'public'])
def postcode():
    '''Get all postcodes.'''

    resp_headers = dict(request.headers)
    if resp_headers.get('Suburb'):
        suburb = resp_headers['Suburb']
        json_doc = to_json(db['postcode'].find({'suburb': suburb.upper()}, {'postcode': 1, '_id': 0}))
    elif resp_headers.get('Postcode'):
        postcode = resp_headers['Postcode']
        json_doc = to_json(db['postcode'].find({'postcode': postcode}, {'suburb': 1, 'lat': 1, "lon": 1, '_id': 0}))
    else:
        json_doc = to_json(db['postcode'].find({}, {'_id': 0}))
    if len(json_doc) < 3:
        return make_response(jsonify({'status': 'failed', 'reason': 'no results found'}), 404)
    print(resp_headers)
    return json_resp(json_doc)
