# app.py
# Main file for Demo App
# author = JP Villavicencio
# email = jefferson.villavicencio@team.telstra.com
# status = Prototype
# last revision = 11 July 2016

from flask import Flask
from demo import index_blueprint, users_blueprint, postcode_blueprint, doc_blueprint
from demo import auto

app = Flask(__name__)
app.debug = True

auto.init_app(app)

app.register_blueprint(index_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(postcode_blueprint)
app.register_blueprint(doc_blueprint)


if __name__ == '__main__':

    app.run()

