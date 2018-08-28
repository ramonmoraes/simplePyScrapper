from scrapper.parser.BaseParser import BaseParser
from bs4 import BeautifulSoup

class MTVnews(BaseParser):
    URL = 'http://www.mtv.com.br/noticias'
    collection_name = 'mtv'

    def __init__(self, url = URL, collection = collection_name ):
        super().__init__(url, collection)

    def get_title(self):
        titleElement = self.elements.find('div', { 'class': 'headline-bar'}).find('h1')
        if titleElement == None:
            return None
        return titleElement.get_text()
    
    def get_text(self):
        content = self.elements.find('div', { 'class': 'blockContent'})
        if content == None:
            return None
        return content.get_text()

    def get_img(self):
        imgElement = self.elements.find('div', {'class' : 'lowres-img'})
        if (imgElement == None):
            return None
        return imgElement.find('img')['src']