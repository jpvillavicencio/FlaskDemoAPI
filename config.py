# config.py
# Config file for Demo App
# author = JP Villavicencio
# email = jefferson.villavicencio@team.telstra.com
# status = Prototype
# last revision = 11 July 2016
import pymongo

con = pymongo.MongoClient("mongodb://localhost:27017/")

mongo_production = con.flask_prod
mongo_test = con.flask_test
