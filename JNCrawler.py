from Crawler import Crawler
from bs4 import BeautifulSoup

class JNCrawler(Crawler):
    URL = 'https://jovemnerd.com.br/nerdbunker/vikings-quinta-temporada-ganha-trailer-brutal/'

    def __init__(self):
        super().__init__(self.URL)

    def get_title(self):
        return self.elements.find('h1', {'class' : 'entry-title'}).get_text()
    
    def get_text(self):
        article = self.elements.find('div', {'class' : 'entry-content'})
        return article.findAll("p" , recursive=True)

    def get_img(self):
        return self.elements.findAll('div', {'class' : 'ytp-cued-thumbnail-overlay-image'})

jn = JNCrawler()
print(jn.get_snippet())