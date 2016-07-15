from flask import Blueprint
from flask_autodoc import Autodoc


doc_blueprint = Blueprint('doc', __name__, url_prefix='/api/doc')
auto = Autodoc()


@doc_blueprint.route('/')
def public_doc():
    return auto.html(groups=['public'], title='Flask Demo API Documentation')