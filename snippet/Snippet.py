from pymongo import MongoClient

from snippet.__init__ import get_db

class Snippet():
    def __init__(self, url, title, text, img):
        self.url = url
        self.title = title
        self.text = text
        self.img = img
    
    def get(self):
        return {
            'url': self.url,
            'title': self.title,
            'text': self.text,
            'img': self.img
        }

    def save_db(self):
        snippets = get_db()['snippets']
        snippets.add_one(self.get())