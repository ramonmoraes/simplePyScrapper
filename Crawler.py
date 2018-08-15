import requests

from bs4 import BeautifulSoup

class Crawler():
    def __init__(self, url):
        pass

    def get_snippet(self):
        return {
            'title': self.get_title(),
            'text': self.get_text(),
            'img': self.get_img()
        }
        