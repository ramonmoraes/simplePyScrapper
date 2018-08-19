import json
from crawler.JNCrawler import JNCrawler


jn = JNCrawler('https://jovemnerd.com.br/nerdbunker/clash-royale-league-latam-adiada/')
jsonData = json.dumps(jn.get_snippet())

with open('data/data.json', 'w') as jsonFile:
    json.dump(jsonData, jsonFile, ensure_ascii=False)