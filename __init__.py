import json

from utils.SnippetWritter import SnippetWritter
from crawler.ArchCrawler import ArchCrawler

arc = ArchCrawler()
links = arc.links
if (len(links) > 40):
    links = links[30:]

snippets = {
    'snippets' : list(filter(lambda link: ArchCrawler(link).get_snippet() != None, links))
}

with open('./data/data.json', 'w') as jsonFile:
    json.dump(snippets, jsonFile, ensure_ascii=False)
