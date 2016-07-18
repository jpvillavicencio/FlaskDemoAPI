# mongo.py
# Config file for Demo App
# author = JP Villavicencio
# email = jefferson.villavicencio@team.telstra.com
# status = Prototype
# last revision = 18 July 2016

import pymongo

# Database location.
con_test = "mongodb://localhost:27017/"
con_prod = "mongodb://192.168.99.100:27017/"

con = pymongo.MongoClient(con_prod)

# Database name.
mongo_test = con.flask_test
