import requests
import re
from bs4 import BeautifulSoup

class Crawler():
    def __init__(self, url):
        self.url = self.clean_url(url)
        self.elements = BeautifulSoup(requests.get(self.url).text, 'html.parser')
        self.domain = self.get_domain(self.url)
        self.links = self.get_links()
        pass
        
    def clean_url(self, url):
        if (url.startswith('/')):
            return self.clean_url(url[1:])
        if (url.startswith('www.')):
            return 'http://' + url
        return url
        
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
        favicon = self.elements.find('link', rel='shortcut icon')
        if (favicon != None):
            return favicon.get('href')
        return None

    def get_snippet(self):
        if (self.get_text() == None or self.get_title() == None):
            return None
        return {
            'title': self.get_title(),
            'text': self.get_text(),
            'img': self.__get_img()
        }
        