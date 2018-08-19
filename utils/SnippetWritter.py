from crawler.JNCrawler import JNCrawler

jn = JNCrawler('https://jovemnerd.com.br/nerdbunker/clash-royale-league-latam-adiada/')
title = jn.get_snippet()['title']
print(title)