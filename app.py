# app.py
# Main file for Demo App
# author = JP Villavicencio
# email = jefferson.villavicencio@team.telstra.com
# status = Prototype
# last revision = 15 July 2016

from flask import Flask
from blueprint import auto
from blueprint import index_blueprint, users_blueprint, postcode_blueprint, doc_blueprint

app = Flask(__name__)
app.debug = True

auto.init_app(app)

# Add new blueprints below
# e.g. app.register_blueprint(<name>_blueprint)
app.register_blueprint(index_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(postcode_blueprint)
app.register_blueprint(doc_blueprint)


if __name__ == '__main__':
    app.run()

