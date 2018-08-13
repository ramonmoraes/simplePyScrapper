import requests
from bs4 import BeautifulSoup

CRAWLER_URL = 'https://www.archdaily.com.br/br/899761/todays-rising-stars-in-design-metropolis-magazine-reveals-their-picks'

class Crawler():
    def __init__(self, url):
        self.get_snippet()
        pass

    def get_snippet(self):
        print(self.parsed.find('h1', {'class':'afd-title-big'}).string)
        pass


c = Crawler(CRAWLER_URL)