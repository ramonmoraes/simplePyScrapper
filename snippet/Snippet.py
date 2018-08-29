from pymongo import MongoClient

from snippet import get_db
from snippet.decorators import info_required

class Snippet:
    def __init__(self, url, title, text, img, collection_name = 'snippet'):
        self.url = url
        self.title = title
        self.text = text
        self.img = img
        self.collection_name = collection_name

    @info_required
    def get_dict(self):
        return {
            'url': self.url,
            'title': self.title,
            'text': self.text,
            'img': self.img
        }

    @info_required
    def save_db(self):
        snippet = self.get_dict()
        print ('Saving {}'.format(snippet))
        get_db()[self.collection_name].insert_one(snippet)