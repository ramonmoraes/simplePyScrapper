import requests
from bs4 import BeautifulSoup

CRAWLER_URL = 'https://www.archdaily.com.br/br/899761/todays-rising-stars-in-design-metropolis-magazine-reveals-their-picks'

class Crawler():
    def __init__(self, options):
        self.html = requests.get(options['url']).text
        self.parsed = BeautifulSoup(self.html, 'html.parser')
        self.cssStructure = options['cssStructure']
        self.get_snippet()
        # self.find_links()
        pass

    # def find_links(self):
    #     links = self.parsed.findAll('a')
    #     print(links)
    #     pass

    def get_snippet(self):
        print(self.parsed.find('h1', {'class':'afd-title-big'}).string)
        pass


cssSnipetStructure = {
    'title': 'h1.afd-title',
    'text': 'article'
}

c = Crawler({
    'url': CRAWLER_URL,
    'cssStructure': cssSnipetStructure
})