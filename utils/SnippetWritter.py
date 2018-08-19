import json
from crawler.JNCrawler import JNCrawler

class SnippetWritter():
    __init__(self, crawler, filePath = 'data/data.json'):
        self.crawler = crawler
        self.filePath = filePath
    
    def writeFile():
        jsonData = json.dumps(self.crawler.get_snippet())
        with open(self.filePath, 'w') as jsonFile:
            json.dump(jsonData, jsonFile, ensure_ascii=False)
