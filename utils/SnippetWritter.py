import json
from crawler.JNCrawler import JNCrawler

class SnippetWritter():
    def __init__(self, crawler, filePath='data/data.json'):
        self.crawler = crawler
        self.filePath = filePath
        self.write()
        pass

    def write():
        snippetList = []
        links = self.crawler.links
        if (len(links) > 40):
            links = links[30:]

        for link in links:
            print('Crawling page :' + link)
            snippet = self.crawler(link).get_snippet() 
            if (snippet != None):
                snippetList.append(snippet)
        
        self.writeFile({ 'snippets': snippetList })

    def writeFile(self, jsonData):
        with open(self.filePath, 'w') as jsonFile:
            json.dump(jsonData, jsonFile, ensure_ascii=False)
