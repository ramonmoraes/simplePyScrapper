import os

from pymongo import MongoClient

def get_db():
    connection_uri = 'mongodb://{}:{}@ds023463.mlab.com:23463/qqrcoisa'
    client = MongoClient(connection_uri.format(os.environ['mongoUser'], os.environ['mongoPassword']))
    db = client['qqrcoisa']
