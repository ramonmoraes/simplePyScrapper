import requests

from Elements import Elements
from bs4 import BeautifulSoup

CRAWLER_URL = 'https://www.archdaily.com.br/br/899761/todays-rising-stars-in-design-metropolis-magazine-reveals-their-picks'

class Crawler():
    def __init__(self, url):
        self.get_snippet()
        self.elements = Elements(requests.get(url).text)
        pass

    def get_snippet(self):
        pass


c = Crawler(CRAWLER_URL)