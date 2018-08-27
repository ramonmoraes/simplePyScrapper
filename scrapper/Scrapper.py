import time
import re

class Scrapper:
    def __init__(self, parser, url, save = False, request_throttle = 1, max_links = 50):
        self.parser = parser
        self.url = url
        self.parser_list = [parser(url)]
        self.save = save
        self.request_throttle = request_throttle
        self.max_links = max_links

    def scrap(self, deepness = 0):
        links = self.parser_list[0].links[:self.max_links]
        print("[Scrapper] Starting with {} links to be parsed".format(len(links)))
        self._scrap(deepness)

    def _scrap(self, deepness):
        already_parsed_links = list(map(lambda parser: parser.url, self.parser_list))
        links_in_parsed_pages = []
        for par in self.parser_list:
            links_in_parsed_pages += par.links

        non_parsed_link = self.get_unique_list(links_in_parsed_pages, already_parsed_links)[:self.max_links]
        print("{} diff links found: ".format(len(non_parsed_link)))

        for link in non_parsed_link:
            time.sleep(self.request_throttle)
            try:
                print('[Scrapper] Parsing {}'.format(link))
                self.parser_list.append(self.parser(link))
            except Exception as err:
                print('[Scrapper] Could not parse {}'.format(link))
                print(err)

        if deepness > 0:
            self._scrap(deepness - 1)
            return

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
            snippet.save_db(self.parser.collection_name)
        else:
            print("[Got snippet]")