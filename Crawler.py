import requests
from bs4 import BeautifulSoup

class Crawler():
    def __init__(self, url):
        self.elements = BeautifulSoup(requests.get(url).text, 'html.parser')
        self.get_links()
        pass

    def get_links(self):
        everySiteLink = self.elements.findAll('a')
        for link in everySiteLink:
            print(link.get('href'))

    def get_snippet(self):
        return {
            'title': self.get_title(),
            'text': self.get_text(),
            'img': self.get_img()
        }
        