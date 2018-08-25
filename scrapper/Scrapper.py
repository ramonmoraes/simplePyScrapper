class Scrapper():
    def __init__(self, parser, url, save = False):
        self.parser = parser
        self.url = url
        self.snippet_list = []
        self.save = save
    
    def get_snippet(self):
        return self.parser.get_snippet()
    
    def scrap(self, deepness = 0):
        links = self.parser(self.url).links
        for link in links:
            print("Scrapping link" + link)
            newParser = self.parser(link)
            self.handle_snippet(newParser.get_snippet())
        
    def handle_snippet(self, snippet):
        s_dict = snippet.get_dict()
        if s_dict == None:
            return
        if self.save == True:
            snippet.save_db()
        else:
            print("[Getting snippet]")
            print(s_dict)