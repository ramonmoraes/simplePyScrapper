import requests
import re

from bs4 import BeautifulSoup
from snippet.Snippet import Snippet

class BaseParser():
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
        if (url.startswith('http')):
            return url
        return 'http://www.' + url
        
    def get_domain(self, url):
        domainRegex = '(?:https?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n?]+)' 
        return re.search(domainRegex, url,re.IGNORECASE).group(1)

    def get_links(self):
        every_site_link = self.elements.findAll('a', href=True)
        same_domain_link_list = []
        for link in every_site_link:
            if self.domain in link.get('href') and self.valid_link(link.get('href')):
                same_domain_link_list.append(link.get('href'))
        return list(set(same_domain_link_list))

    def valid_link(self, url):
        valid_link_regex = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        if re.match(valid_link_regex, url):
            return True
        return False

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
        return Snippet(
            self.url,
            self.get_title(),
            self.get_text(),
            self.__get_img()
        )
        