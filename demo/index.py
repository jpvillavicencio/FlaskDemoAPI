from flask import Blueprint, render_template
from .doc import auto

index_blueprint = Blueprint('index', __name__)


@index_blueprint.route('/')
@auto.doc(groups=['public'])
def index():
    return render_template('index.html')
