import requests

from Elements import Elements
from bs4 import BeautifulSoup

CRAWLER_URL = 'https://www.archdaily.com.br/br/899761/todays-rising-stars-in-design-metropolis-magazine-reveals-their-picks'

class Crawler():
    def __init__(self, url):
        self.elements = Elements(requests.get(url).text)
        pass

    def get_snippet(self):
        return {
            'title': self.get_title(),
            'text': self.get_text(),
            'img': self.get_img()
        }
        