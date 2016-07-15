# blueprint/users.py
# User Routes
# description = get and post method for users
# author = JP Villavicencio
# email = jefferson.villavicencio@team.telstra.com
# status = Prototype
# last revision = 15 July 2016

from flask import Blueprint, abort, request, make_response, jsonify
from .doc import auto
from .demo import json_resp, to_json
import mongo

users_blueprint = Blueprint('users', __name__, url_prefix='/api/users')
db = mongo.mongo_test


@users_blueprint.route('/upload', methods=['POST'])
@auto.doc(groups=['users', 'public'])
def users_post():
    '''Upload users. Requires the following fields: str:fname, str:lname, str:postcode, str:dob'''
    resp_headers = dict(request.headers)
    print(request.method)
    user = {}
    resp = {'status': 'success'}
    if resp_headers.get('Fname') or resp_headers.get('Lname') or resp_headers.get('Postcode') or resp_headers.get('Dob'):
        if resp_headers.get('Fname') and resp_headers.get('Lname') and resp_headers.get('Postcode') and resp_headers.get('Dob'):
            user['fname'] = resp_headers['Fname'].capitalize()
            user['lname'] = resp_headers['Lname'].capitalize()
            user['postcode'] = resp_headers['Postcode']
            user['dob'] = resp_headers['Dob']
            print(user)
            return jsonify(resp), 201
        else:
            abort(400)
    else:
        abort(404)
        # db['users'].insert(user)


@users_blueprint.route('/', methods=['GET'])
@auto.doc(groups=['users', 'public'])
def users_get():
    '''Get all users. Returns fname, lname, postcode, dob'''
    json_doc = to_json(db['users'].find({}, {'_id': 0}))
    if len(json_doc) < 3:
        abort(404)
    return json_resp(json_doc)


@users_blueprint.route('/<postcode>', methods=['GET'])
@auto.doc(groups=['users', 'public'])
def user_postcode(postcode):
    '''Gets users from certain postcode. Returns fname, lname'''
    if postcode:
        json_doc = to_json(db['users'].find({'postcode': postcode}, {'fname': 1, 'lname': 1, '_id': 0}))
    if len(json_doc) < 3:
        abort(404)
    return json_resp(json_doc)


@users_blueprint.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'status': 'failed', 'reason': 'no results found'}), 404)


@users_blueprint.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'status': 'failed', 'reason': 'missing field'}), 400)
