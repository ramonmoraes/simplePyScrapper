from pymongo import MongoClient

from snippet.__init__ import get_db
from snippet.decorators import info_required
    
class Snippet():
    def __init__(self, url, title, text, img):
        self.url = url
        self.title = title
        self.text = text
        self.img = img

    @info_required
    def get_dict(self):
        return {
            'url': self.url,
            'title': self.title,
            'text': self.text,
            'img': self.img
        }
        
    @info_required
    def save_db(self, collection_name = 'snippets'):
        snippet = self.get_dict()
        print ('Saving {}'.format(snippet))
        get_db()[collection_name].insert_one(snippet)