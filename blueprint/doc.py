# blueprint/doc.py
# API Docs
# description = Auto generates API documentation for the project
# author = JP Villavicencio
# email = jefferson.villavicencio@team.telstra.com
# status = Prototype
# last revision = 15 July 2016

from flask import Blueprint
from flask_autodoc import Autodoc


doc_blueprint = Blueprint('doc', __name__, url_prefix='/api/doc')
auto = Autodoc()


@doc_blueprint.route('/')
def public_doc():
    #return auto.html(groups=['public'], title='Flask Demo API Documentation', template="autodoc_custom.html")
    return auto.html(groups=['public'], title='Flask Demo API Documentation')