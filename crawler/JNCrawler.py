from crawler.Crawler import Crawler
from bs4 import BeautifulSoup

class JNCrawler(Crawler):
    URL = 'https://jovemnerd.com.br/nerdbunker/'
    def __init__(self, url = URL):
        super().__init__(url)

    def get_sub_path(self):
        return '/nerdbunker'

    def get_title(self):
        return self.elements.find('h1', {'class' : 'entry-title'}).get_text()
    
    def get_text(self):
        article = self.elements.find('div', {'class' : 'entry-content'})
        articles = article.findAll("p" , recursive=True)
        text = ''
        for paragraphs in articles:
            text += paragraphs.get_text()
        return text

    def get_img(self):
        return self.elements.find('div', {'class' : 'ytp-cued-thumbnail-overlay-image'})