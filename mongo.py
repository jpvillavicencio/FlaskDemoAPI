# mongo.py
# Config file for Demo App
# author = JP Villavicencio
# email = jefferson.villavicencio@team.telstra.com
# status = Prototype
# last revision = 15 July 2016

import pymongo

# Database location.
con = pymongo.MongoClient("mongodb://localhost:27017/")

# Database name.
mongo_production = con.flask_prod
mongo_test = con.flask_test
