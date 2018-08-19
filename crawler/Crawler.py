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
        same_domain_link_list = []
        for link in every_site_link:
            if self.domain in link.get('href'):
                same_domain_link_list.append(link.get('href'))
        return list(set(same_domain_link_list))

    def __get_img(self):
        img = self.get_img()
        if (img != None):
            return img
        return self.get_favicon()
    
    def get_favicon(self):
        return self.elements.find('link', rel='shortcut icon').get('href')

    def get_snippet(self):
        return {
            'title': self.get_title(),
            'text': self.get_text(),
            'img': self.__get_img()
        }
        