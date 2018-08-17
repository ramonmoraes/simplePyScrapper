import requests
import re
from bs4 import BeautifulSoup

class Crawler():
    def __init__(self, url):
        self.elements = BeautifulSoup(requests.get(url).text, 'html.parser')
        self.domain = self.get_domain(url)
        self.links = self.get_links()
        pass

    def get_domain(self, url):
        domainRegex = '(?:https?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n?]+)' 
        return re.search(domainRegex, url,re.IGNORECASE).group(1)

    def get_links(self):
        every_site_link = self.elements.findAll('a', href=True)
        link_list = []
        for link in every_site_link:
            if self.domain in link.get('href'):
                link_list.append(link.get('href'))
        return link_list

    def get_snippet(self):
        return {
            'title': self.get_title(),
            'text': self.get_text(),
            'img': self.get_img()
        }
        