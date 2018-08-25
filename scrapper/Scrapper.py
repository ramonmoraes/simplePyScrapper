import time
import re

class Scrapper():
    def __init__(self, parser, url, save = False, request_throttle = 1, max_links = 5):
        self.parser = parser
        self.url = url
        self.parser_list = [parser(url)]
        self.save = save
        self.request_throttle = request_throttle
        self.max_links = max_links
    
    def scrap(self, deepness = 0):
            links = self.parser_list[0].links[:self.max_links]
            print("[Scrapper] Starting with {} links to be parsed".format(len(links)))
            self._scrap(deepness, links)

    def _scrap(self, deepness, links):
        diff_links = []
        for new_parser in self.parser_list:
            diff_links = self.get_unique_list(new_parser.links, links)
        diff_links = diff_links[:self.max_links]
        print("{} diff links found: ".format(len(links)))

        for link in diff_links:
            print("[Scrapper] scrapping {}".format(link))
            self.parser_list.append(self.parser(link))
            time.sleep(self.request_throttle)
        print("{} links were parsed".format(len(links)))
        if deepness > 0:
            self._scrap(deepness - 1, links + diff_links)
            
        self.parse()

    def parse(self):
        print("[Scrapper] Start parsing")
        for parser in self.parser_list:
            self.handle_snippet(parser.get_snippet())
    
    def get_unique_list(self, appended_list, compared_list):
        return list(set(appended_list) - set(compared_list))

    def handle_snippet(self, snippet):
        s_dict = snippet.get_dict()
        if s_dict == None:
            return
        if self.save == True:
            snippet.save_db()
        else:
            print("[Got snippet]")