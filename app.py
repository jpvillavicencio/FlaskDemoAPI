# app.py
# Main file for Demo App
# author = JP Villavicencio
# email = jefferson.villavicencio@team.telstra.com
# status = Prototype
# last revision = 11 July 2016

from flask import Flask, render_template, jsonify, abort, make_response, request
import config
from flask_cors import CORS, cross_origin
from demo import demo

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
db = config.mongo_test


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/users/', methods=['POST'])
@cross_origin(origin='*', headers=['Content-Type'])
def users_post():
    resp_headers = dict(request.headers)
    print (request.method)
    user = {}
    resp = {'status': 'success'}
    if resp_headers.get('Fname') or resp_headers.get('Lname') or resp_headers.get('Postcode') or resp_headers.get('Dob'):
        if resp_headers.get('Fname') and resp_headers.get('Lname') and resp_headers.get('Postcode') and resp_headers.get('Dob'):
            user['fname'] = resp_headers['Fname'].capitalize()
            user['lname'] = resp_headers['Lname'].capitalize()
            user['postcode'] = resp_headers['Postcode']
            user['dob'] = resp_headers['Dob']
            print (user)
            return jsonify(resp),201
        else:
            abort(400)
    else:
        abort(404)
        #db['users'].insert(user)


@app.route('/api/users/', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type'])
def users_get():
    resp_headers = dict(request.headers)
    print (request.method)
    if resp_headers.get('Postcode'):
        postcode = resp_headers['Postcode']
        json_doc = demo.to_json(db['users'].find({'postcode': postcode}, {'fname': 1, 'lname': 1, '_id': 0}))
        if len(json_doc) < 3:
            abort(404)
    else:
        json_doc = demo.to_json(db['users'].find({}, {'_id': 0}))
    print ('method get')
    return demo.json_resp(json_doc)


@app.route('/api/postcode/', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type'])
def postcode():
    resp_headers = dict(request.headers)

    if resp_headers.get('Suburb'):
        suburb = resp_headers['Suburb']
        json_doc = demo.to_json(db['postcode'].find({'suburb': suburb.upper()}, {'postcode': 1, '_id': 0}))
    elif resp_headers.get('Postcode'):
        postcode = resp_headers['Postcode']
        json_doc = demo.to_json(db['postcode'].find({'postcode': postcode}, {'suburb': 1, 'lat': 1, "lon": 1, '_id': 0}))
    else:
        json_doc = demo.to_json(db['postcode'].find({}, {'_id': 0}))
    if len(json_doc) < 3:
        abort(404)
    print (resp_headers)
    return demo.json_resp(json_doc)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'status': 'failed', 'reason': 'no results found'}), 404)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'status': 'failed', 'reason': 'missing field'}), 400)


if __name__ == '__main__':
    app.run()
