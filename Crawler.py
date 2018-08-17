import requests
import re
from bs4 import BeautifulSoup

class Crawler():
    def __init__(self, url):
        self.elements = BeautifulSoup(requests.get(url).text, 'html.parser')
        self.domain = self.get_domain(url)
        self.links = self.get_links()
        print(self.links)
        pass

    def get_domain(self, url):
        domainRegex = '(?:https?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n?]+)' 
        return re.search(domainRegex, url,re.IGNORECASE).group(1)

    def get_links(self):
        everySiteLink = self.elements.findAll('a')
        link_list = []
        for link in everySiteLink:
            if self.domain in link.get('href'):
                link_list.append(link.get('href'))
        return link_list

    def get_snippet(self):
        return {
            'title': self.get_title(),
            'text': self.get_text(),
            'img': self.get_img()
        }
        