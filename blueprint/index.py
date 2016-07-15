# blueprint/index.py
# Index routes
# author = JP Villavicencio
# email = jefferson.villavicencio@team.telstra.com
# status = Prototype
# last revision = 15 July 2016

from flask import Blueprint, render_template, jsonify
from .doc import auto

index_blueprint = Blueprint('index', __name__)


@index_blueprint.route('/')
@auto.doc(groups=['public'])
def index():
    '''Returns home page.'''
    return render_template('index.html')

@index_blueprint.route('/api')
@auto.doc(groups=['public'])
def api():
    '''Returns API status.'''
    return jsonify({'status': 'alive', 'hello': 'world'}), 200
