from crawler import Crawler
from bs4 import BeautifulSoup

class ArchCrawler(Crawler):
    URL = 'https://www.archdaily.com.br/br/899761/todays-rising-stars-in-design-metropolis-magazine-reveals-their-picks'

    def __init__(self):
        super().__init__(self.URL)

    def get_title(self):
        return self.elements.find('h1', {'class': 'afd-title-big'}).get_text()
    
    def get_text(self):
        article = self.elements.find('article')
        return article.findAll("p" , recursive=True)

    def get_img(self):
        return self.elements.find('picture').find('img')['src']