import os

from pymongo import MongoClient

def get_db():
    client = MongoClient(connection_uri.format(os.environ['mongoUser'], os.environ['mongoPassword']))
    db = client['qqrcoisa']
