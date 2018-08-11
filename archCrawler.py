import requests
from bs4 import BeautifulSoup

CRAWLER_URL = 'https://www.archdaily.com.br/br/899761/todays-rising-stars-in-design-metropolis-magazine-reveals-their-picks'

class Crawler():
    def __init__(self, url):
        self.html = requests.get(url).text
        pass

c = Crawler(CRAWLER_URL)
print(c.html)