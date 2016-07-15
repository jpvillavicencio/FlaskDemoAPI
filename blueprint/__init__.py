# app.py
# Main file for Demo App
# author = JP Villavicencio
# email = jefferson.villavicencio@team.telstra.com
# status = Prototype
# last revision = 15 July 2016

# Import new blueprints below.
# from .<name> import <name>_blueprint
from .postcode import postcode_blueprint
from .users import users_blueprint
from .index import index_blueprint
from .doc import doc_blueprint, auto
from .demo import to_json, json_resp
