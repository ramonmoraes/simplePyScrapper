class Scrapper():
    def __init__(self, parser, save = False):
        self.parser = parser
        self.links = parser.links
        self.snippet_list = []
    
    def get_snippet(self):
        return self.parser.get_snippet().get_dict()
    
    def scrap(self, deepness = 0):
        for link in self.links:
            print("Scrapping link" + link)
